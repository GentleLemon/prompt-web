<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const emit = defineEmits(['deletePrompt'])

const props = defineProps({
    my: {
        type: [Boolean]
    },
    prompt: {
        type: [Object]
    }
})

async function deletePrompt(id) {
    await $fetch('http://127.0.0.1:8000/api/v1/prompts/' + id + '/delete/', {
        method: 'DELETE',
        headers: {
            'Authorization': 'token ' + userStore.user.token,
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        console.log('response', response)

        emit('deletePrompt', id)
    })
    .catch(error => {
        console.log(error)
    })
}

async function copyContent() {
    try {
        await navigator.clipboard.writeText(prompt.description)
        alert('Content copied to clipboard')
    } catch (err) {
        console.error('Failed to copy text: ', err)
    }
}


</script>

<template>
    <div class="p-6 bg-gray-100 rounded-xl shadow-md">
        <div class="flex items-center justify-between mb-4">
            <div>
                <h3 class="mb-2 text-xl font-semibold">{{ prompt.title }}</h3>
                <p class="text-gray-600">{{ prompt.category }}</p>
            </div>
            <p>Posted {{ prompt.created_at }} by {{ prompt.company_name }}</p>
        </div>

        <div class="mb-4">
            <p>{{ prompt.description }}</p>
        </div>

        <div class="flex items-center space-x-4">
            <button @click="copyContent" class="py-2 px-4 bg-blue-500 text-white rounded-lg">
                Copy Content
            </button>
            <NuxtLink v-bind:to="'/browse/' + prompt.id" class="py-2 px-4 bg-teal-700 text-white rounded-lg">Details</NuxtLink>
            <NuxtLink v-bind:to="'/editprompt/' + prompt.id" class="py-2 px-4 bg-cyan-700 text-white rounded-lg" v-if="my">Edit</NuxtLink>
            <button @click="deletePrompt(prompt.id)" class="py-2 px-4 bg-rose-700 text-white rounded-lg" v-if="my">Delete</button>
        </div>
    </div>
</template>
