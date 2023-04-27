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
</script>

<template>
    <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
        <div>
            <h3 class="mb-2 text-xl font-semibold">{{ prompt.title }}</h3>
            <p class="text-gray-600">{{ prompt.company_name }}</p>
        </div>

        <div>
            <p class="mb-2">{{ prompt.position_location }}</p>
            <p>{{ prompt.position_salary }}</p>
        </div>

        <div>
            <p>Posted {{ prompt.created_at_formatted }}</p>
        </div>

        <div class="space-x-4">
            <NuxtLink v-bind:to="'/browse/' + prompt.id" class="py-4 px-6 bg-teal-700 text-white rounded-xl">Details</NuxtLink>
            <NuxtLink v-bind:to="'/editprompt/' + prompt.id" class="py-4 px-6 bg-cyan-700 text-white rounded-xl" v-if="my">Edit</NuxtLink>
            <a @click="deletePrompt(prompt.id)" class="py-4 px-6 bg-rose-700 text-white rounded-xl" v-if="my">Delete</a>
        </div>
    </div>
</template>