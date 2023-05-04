<template>
  <v-app :theme="$colorMode.value">
    <NavigationDrawer />
s
    <v-app-bar app>
      <v-toolbar-title>ChatGPT</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/login" text>Login</v-btn>
      <v-btn to="/signup" text>Register</v-btn>
    </v-app-bar>

    <v-main>
      <slot />
    </v-main>
  </v-app>
</template>
