import { ref } from 'vue';

const task = ([]);

function addTask() {
    var taskInput = document.getElementById("taskInput");
    var taskList = document.getElementById("TaskList");

    if (taskInput.value.trim() !== "") {
        var li = document.createElement("li");

        var taskTitle = document.createElement("span");
        taskTitle.textContent = taskInput.value;

        li.appendChild(taskTitle);
        taskList.appendChild(li);

        taskInput.value = ""; 
    } else {
        alert("Il n'y a pas d'éléments à ajouter !");
    }
}
