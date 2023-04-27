<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const router = useRouter()
let prompts = ref()

onMounted(() => {
    if (!userStore.user.isAuthenticated) {
        router.push('/login')
    } else {
        getPrompts()
    }
})

useSeoMeta({
    title: 'My prompts',
    ogTitle: 'My prompts',
    description: 'The description'
})

async function getPrompts() {
    await $fetch('http://127.0.0.1:8000/api/v1/prompts/my', {
        headers: {
            'Authorization': 'token ' + userStore.user.token,
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        prompts.value = response
    })
    .catch(error => {
        console.log('error', error)
    })
}

function deletePrompt(id) {
    console.log('id', id)

    prompts.value = prompts.value.filter(prompt => prompt.id !== id)
}
</script>

<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">My prompts</h1>

        <div class="space-y-4">
            <Prompt
                v-for="prompt in prompts"
                :key="prompt.id"
                :prompt="prompt" 
                :my="true"
                v-on:deletePrompt="deletePrompt(prompt.id)"
            />
        </div>
    </div>
</template>