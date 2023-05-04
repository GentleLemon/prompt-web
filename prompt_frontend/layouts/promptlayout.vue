<script setup>
import {useUserStore} from '@/stores/user'

const userStore = useUserStore()

function logout() {
    userStore.removeToken()
}

const isLoggedIn = computed(() => userStore.isLoggedIn)
</script>


<template>
  <v-app :theme="$colorMode.value" class="mx-auto" max-width="448">

      <v-app-bar
        color="#ececf1"
        density="compact"
      >
        <template v-slot:prepend>
          <v-app-bar-nav-icon class="text-white"></v-app-bar-nav-icon>
        </template>
        <v-toolbar-title>
            <router-link class="no-underline text-white" to="/">ChatGPT</router-link>
        </v-toolbar-title>

    <v-spacer></v-spacer>
    <template v-if="!isLoggedIn">
      <v-btn class="no-underline text-white" to="/account/signin">登录</v-btn>
      <v-btn class="no-underline text-white" to="/account/signup">注册</v-btn>
    </template>
    <template v-else>
      <v-btn color="secondary" @click="logout">登出</v-btn>
    </template>

    </v-app-bar>

    <v-main>
      <slot />
    </v-main>

  <v-footer class="bg-grey-lighten-1">
    <v-row justify="center" no-gutters>
      <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        variant="text"
        class="mx-2"
        rounded="xl"
      >
        {{ link }}
      </v-btn>
      <v-col class="text-center mt-4" cols="12">
        <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener noreferrer">苏ICP备***号-1</a>
      </v-col>
    </v-row>
  </v-footer>
  </v-app>
</template>

<style>
  .no-underline {
    text-decoration: none;
  }
.app-header {
    align-items: center;
    background-color: #fff;
    border-bottom: 1px solid #ececf1;
    display: flex;
    height: 60px;
    height: var(--app-header-height);
    justify-content: space-between;
    overflow: auto;
    padding: 0 24px;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 100;
}
</style>

<script>
  export default {
    data: () => ({
      links: [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Blog',
        'Contact Us',
      ],
    }),
  }
</script>
