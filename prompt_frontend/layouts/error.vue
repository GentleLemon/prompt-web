<template>
  <v-app>
    <v-navigation-drawer app>
      <!-- Left menu content -->
    </v-navigation-drawer>
    <v-app-bar app>
      <v-toolbar-title>
        <v-btn text :to="{ name: 'overview' }">
          <v-icon>your_logo_icon</v-icon>
        </v-btn>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text>Support</v-btn>
      <v-btn text>Login</v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <!-- Page content -->
      </v-container>
      <v-footer>
        <v-row>
          <v-col>
            <v-icon>developer_forum_icon</v-icon>
            <div class="mt-2">Developer forum</div>
            <div class="mt-2">Ask questions and discuss topics with other developers.</div>
            <div class="mt-2">
              <v-btn text href="https://community.openai.com" target="_blank">Visit developer forum</v-btn>
              <v-btn text :to="{ name: 'ambassadors' }">Meet ambassadors</v-btn>
            </div>
          </v-col>
          <v-col>
            <v-icon>service_status_icon</v-icon>
            <div class="mt-2">Service status</div>
            <div class="mt-2">Check the status of OpenAI services.</div>
            <div class="mt-2">
              <v-btn text href="https://status.openai.com" target="_blank">Visit status page</v-btn>
            </div>
          </v-col>
        </v-row>
      </v-footer>
    </v-main>
  </v-app>
</template>
