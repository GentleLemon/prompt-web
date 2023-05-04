<template>
  <v-app>
    <v-main>
      <NavigationDrawer />
<!--        <v-container>-->
          <Welcome />
          <WelcomeCard />
          <ChatConversation :conversation="conversation"/>
<!--        </v-container>-->
    </v-main>
  </v-app>
</template>


<script setup>
import ChatConversation from '~/components/chat/Conversation.vue';
import NavigationDrawer from '~/components/chat/NavigationDrawer.vue';
import WelcomeCard from '~/components/chat/WelcomeCard.vue';
import Welcome from '~/components/chat/Welcome.vue';

import { useUser } from '~/composables/states'

const user = useUser()

</script>
