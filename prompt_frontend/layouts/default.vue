<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

function logout() {
    userStore.removeToken()
}
</script>


<template>
    <div class="flex flex-col min-h-screen">
        <nav class="p-6 bg-teal-800">
            <div class="container mx-auto flex items-center justify-between">
                <NuxtLink to="/" class="text-xl text-white">ChatGPT提示</NuxtLink>
                <div class="hidden md:flex items-center space-x-4">
                    <NuxtLink to="/" class="text-white hover:text-teal-300">Home</NuxtLink>
                    <NuxtLink to="/browse" class="text-white hover:text-teal-300">Browse</NuxtLink>
<!--                    <NuxtLink to="/about" class="text-white hover:text-teal-300">About</NuxtLink>-->
                </div>
                <div class="flex items-center space-x-4">
                    <template v-if="userStore.user.isAuthenticated">
                        <NuxtLink to="/myprompts" class="text-white hover:text-teal-300">My prompts</NuxtLink>
                        <NuxtLink to="/createprompt" class="text-white hover:text-teal-300">Create prompt</NuxtLink>
                        <a v-on:click="logout" class="text-white hover:text-teal-300">Log out</a>
                    </template>
                    <template v-else>
                        <NuxtLink to="/login" class="text-white hover:text-teal-300">Log in</NuxtLink>
                        <NuxtLink to="/signup" class="text-white hover:text-teal-300">Sign up</NuxtLink>
                    </template>
                </div>
            </div>
        </nav>

        <div class="flex-grow">
            <slot />
        </div>

        <footer class="p-6 flex items-center justify-between bg-gray-900">
            <p class="text-gray-300">Copyright (c) 2023 - ChatGPT提示</p>
        </footer>
    </div>
</template>
