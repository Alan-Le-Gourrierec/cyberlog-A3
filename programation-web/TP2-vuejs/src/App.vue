<script setup>
import { ref, onMounted, computed, watch } from 'vue'

const todos = ref([])
const name = ref('')

const input_content = ref('')

const todos_asc = computed(() => todos.value.sort((a,b) =>{
	return a.createdAt - b.createdAt
}))

watch(name, (newVal) => {
	localStorage.setItem('name', newVal)
})

watch(todos, (newVal) => {
	localStorage.setItem('todos', JSON.stringify(newVal))
}, {
	deep: true
})

const addTodo = () => {
	if (input_content.value.trim() === '') {
		return
	}

	todos.value.push({
		content: input_content.value,
		done: false,
		editable: false,
		
		createdAt: new Date().getTime()
	})
}

const removeTodo = (todo) => {
	todos.value = todos.value.filter((t) => t !== todo)
}

const valideToto = (todo) => {
	todo.color = 'green';

}
onMounted(() => {
	name.value = localStorage.getItem('name') || ''
	todos.value = JSON.parse(localStorage.getItem('todos')) || []
})
</script>

<template>
	<!--
		partie dédié à la création des éléments avec une patie 
			- input de text
			- un bouton pour valider
	-->
	<section class="create-todo">
		<h3>TODO List</h3>

		<form id="new-todo-form" @submit.prevent="addTodo">
			<h4>Quelle tache voulez-vous ajouter ?</h4>
			<!-- 
				génération de la zone de text avec les divers éléments interne :
					- placeholder permet de mettre un texte de remplacement temporaire
					- v-model permet la gestion par vue des divers éléments	 
			-->
			<input 
				type="text" 
				name="content" 
				id="content" 
				placeholder="le nom de votre tache"
				v-model="input_content"/>
			<input type="submit" value="Add todo" class=""/>
		</form>
	</section>
	<!-- création des items de notre todo liste -->
	<section class="todo-list">
		<div class="list">
			<h3>TODO LIST</h3>
				<div v-for="todo in todos_asc" :class="`todo-item ${todo.done && 'done'}`" :style="{backgroundColor: todo.color}">
					<div class="container">
						<div class="container">
							<input type="checkbox" v-model="todo.done">
						</div class="container">
						<div class="todo-content">
							<input type="text" v-model="todo.content">
						</div>
						<div class="button-delete">
							<button class="delete button" @click="removeTodo(todo)"> delete </button>
						</div>
					</div>
				</div>
			</div>
	</section>

</template>
