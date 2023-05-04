<script setup>
import Prompt from "~/components/prompt/prompt.vue";
const { data: prompts } = await useFetch('http://127.0.0.1:8000/api/v1/prompts/newest/');
</script>

<template>
  <v-main>
    <v-container fluid class="py-20 text-center" color="teal darken-3" text-color="white">
      <h1 class="mb-12 text-5xl">优秀的ChatGPT提示</h1>

      <v-btn to="/browse" outlined rounded class="mx-2">Browse</v-btn>
      <!--<v-btn to="/about" outlined rounded class="mx-2">About</v-btn>-->
    </v-container>

    <v-container fluid class="py-10 px-6">
      <h2 class="mb-8 text-2xl text-center">最常用的提示</h2>
      <v-row>
        <v-col cols="12" sm="6" md="4" lg="3" v-for="prompt in prompts" :key="prompt.id">
          <Prompt :prompt="prompt" class="prompt-container">
          </Prompt>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<style scoped>
.prompt-container {
  width: 100%;
  height: 300px;
}
</style>
