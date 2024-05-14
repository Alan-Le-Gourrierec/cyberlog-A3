#include <openssl/sha.h>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <regex>

using namespace std;
namespace fs = filesystem;

string nameLog(const string& directory)
{
    smatch matches;
    regex pattern("([a-aZ-Z]+)(\\d+)\\.txt");
    int number = -1;

    try
    {
        for(const auto& entry : fs::directory_iterator(directory))
        {
            if(fs::is_regular_file(entry))
            {
                string file_name = entry.path().filename().string(); 
                cout<< file_name << endl;
                if(regex_search(file_name, matches, pattern))
                {
                    if(stoi(matches[2].str())>number){number = stoi(matches[2].str());}
                }
            }
        }
    }
    catch (const exception& e)
    {
        cerr << "Erreur : " << e.what() << std::endl;
    }

    if(number>0)
    {
        return "log" + to_string(number) + ".txt";
    }
    else
    {
        return "log0.txt";
    } 
}

string signatureSha(const string& filePath)
{
    FILE* f = fopen(filePath.c_str(), "rb");
    if (!f) {
        cerr << "couldn't open " << filePath << "\n";
        return "";
    }

    SHA_CTX ctx;
    size_t len;
    unsigned char buffer[BUFSIZ];
    SHA1_Init(&ctx);

    do {
        len = fread(buffer, 1, BUFSIZ, f);
        SHA1_Update(&ctx, buffer, len);
    } while (len == BUFSIZ);

    SHA1_Final(buffer, &ctx);
    fclose(f);

    string sha1String;
    char hex[3];
    for (len = 0; len < SHA_DIGEST_LENGTH; ++len) {
        sprintf(hex, "%02x", buffer[len]);
        sha1String += hex;
    }

    return sha1String;
}

void scanDirectory(int argc, char** argv, const string& directory, const string& file_name)
{
    ofstream out_file(file_name, ios::app);

    if (not(out_file.is_open()))
    {
        cerr << "ERREUR, impossible d'ouvrir le fichier " << file_name << endl;
        return;
    }

    try {
        for (const auto& entry : fs::directory_iterator(directory))
        {
            if (fs::is_regular_file(entry))
            {
                out_file << entry.path().filename() << " " <<signatureSha(entry.path().string()) << endl;
            }
            if (fs::is_directory(entry))
            {
                out_file << entry.path().filename() <<endl;
                scanDirectory(argc, argv, entry.path(), file_name);
            }
        }
    } catch (const fs::filesystem_error& e) {
        cerr << "Erreur : " << e.what() << endl;
    }
}

int main(int argc, char** argv)
    {
    if (argc < 2) {
        cerr << "usage: " << argv[0] << " <directory>\n";
        return 1;
    }
    

    string directoryPath = argv[1];
    string outputFileName = "resultat/log/" + nameLog(directoryPath);
    cout<<outputFileName<<endl;

    scanDirectory(argc, argv, directoryPath, outputFileName);

    return 0;
}