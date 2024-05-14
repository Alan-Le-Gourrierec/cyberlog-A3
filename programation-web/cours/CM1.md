<!DOCTYPE html>
<html>
    <div id="header">
    <cen>
        <img src="images/Logo_ensibs.png" alt="Logo_ensibs" style="width: auto;">
    </div>
    <div>
    <body>
        <hr>
            <h1><strong>TP0 : Introduction au langage HTML</strong></h1>
        <hr>
		<div>
			<h2>Remarques</h2>
		</div>
        <form action="/test.php">
            <fieldset>
                <table>
                        <legend>Information personel</legend>
                    <tr>
                        <td><label for="nom">Nom</label></td>
                        <td><input type="text" id="nom" name="nom"></td>
                    </tr>
                    <tr>
                        <td><label for="prenom">Prenom</label></td>
                        <td><input type="text" id="prenom" name="prenom"></td>
                    </tr>
                    <tr>
                        <td><label for="telephone">Tel</label></td>
                        <td><input type="tel" id="telephone" name="telephone"></td>
                    </tr>
                    <tr>
                        <td><label for="mail">Email</label></td>
                        <td><input type="email" id="mail" name="mail"></td>
                    </tr>
                    <tr>
                        <td><label for="birth">Date de naissance</label>
                        <input type="date" id="birth" name="birth"></td>
                        <td><label for="nation"> Pays</label>
                        <select id="cars" name="cars">
                            <option value="france">bagette</option>
                            <option value="allemagne">Betonplate</option>
                            <option value="GB">rossbeaf</option>
                            <option value="russie">vodka</option>
                        </select>
                    </td>
                    </tr>
                </table>
            </fieldset>
            <fieldset>
                <legend>Adresse</legend>
                <table>
                    <tr>
                        <td><label for="streat">Rue</label></td>
                        <td><input type="text" id="streat" name="streat"></td>
                    </tr>
                    <tr>
                        <td><label for="code">Code Postal</label></td>
                        <td><input type="number" id="code" name="code"></td>
                        <td><label for="ville">Ville</label></td>
                        <td><input type="text" id="ville" name="ville" list="villes"></td>
                    </tr>
                </table>
            </fieldset>
            <fieldset>
                <legend>Sport pratiqué</legend>
                <input type="checkbox" id="football" name="football" value="football">
                <label for="football">Football</label><br>
                <input type="checkbox" id="basketball" name="basketball" value="basketball">
                <label for="basketball">Basketball</label><br>
                <input type="checkbox" id="tennis" name="tennis" value="tennis">
                <label for="tennis">Tennis</label><br>
            </fieldset>
            <fieldset>
                <legend>Status</legend>
                <input type="radio" id="celibataire" name="rrrrr" value="Célibataire" checked>
                <label for="divorce">Célibataire</label><br>
                <input type="radio" id="marie" name="rrrrr" value="Marié">
                <label for="divorce">Marié</label><br>
                <input type="radio" id="divorce" name="rrrrr" value="Divorcé">
                <label for="divorce">Divorcé</label><br>
            </fieldset>
            <fieldset>
                <legend>Commentaire</legend>
                <label for="comment">Vous pouvez laisser un commentaire ici</label><br>
                <form action="action_page.php">
                    <textarea name="message" rows="10" cols="50" placeholder="comment">
                    </textarea>
                </form> 
            </fieldset>
            <fieldset>
                <legend>Joindre un fichier</legend>
                <label for="fichier">Vous pouvez joindre votre CV (format pdf ou word)</label><br>
                <input type="file" id="fichier" name="fichier">
            </fieldset>
        </form> 
        <datalist id="villes">
            <option value="Nantes"></option>
            <option value="Lorient"></option>
            <option value="Brest"></option>
            <option value="Hennebont"></option>
            <option value="Rennes"></option>
            <option value="Plougelmeneln"></option>
        </datalist>
    </body>
</html>



