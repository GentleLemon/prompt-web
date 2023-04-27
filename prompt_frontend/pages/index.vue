<script setup>
 const { data: prompts } = await useFetch('http://127.0.0.1:8000/api/v1/prompts/newest/')
</script>

<template>
    <div>
        <div class="py-20 px-6 bg-teal-700 text-center">
            <h1 class="mb-12 text-5xl text-white">优秀的ChatGPT提示</h1>

            <NuxtLink to="/browse" class="inline-block py-4 px-8 bg-teal-900 text-white rounded-xl">Browse</NuxtLink>
        </div>

        <div class="py-10 px-6">
            <h2 class="mb-8 text-2xl text-center">Newest prompts</h2>

            <div class="flex flex-row space-x-4">
                <Prompt
                    v-for="prompt in prompts"
                    v-bind:key="prompt.id"
                    v-bind:prompt="prompt"
                    class="prompt-container"
                >
                    <div class="space-y-4 h-full">
                        <!-- Any additional content or elements you want to include within the Prompt component -->
                    </div>
                </Prompt>
            </div>


        </div>

    </div>
</template>

<style scoped>
.prompt-container {
    width: 100%;
    height: 300px;
}
</style>