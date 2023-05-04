<template>
  <div>
    <NavigationDrawer />
    <Welcome />
    <WelcomeCard />
    <ChatConversation :conversation="conversation" />
<!--    <Prompt />-->
  </div>
</template>

<script>
import ChatConversation from '~/components/chat/Conversation.vue';
import ApiKeyDialog from '~/components/chat/ApiKeyDialog.vue';
import ModelDialog from '~/components/chat/ModelDialog.vue';
import ModelParameters from '~/components/chat/ModelParameters.client.vue';
import MsgContent from '~/components/chat/MsgContent.vue';
import MsgEditor from '~/components/chat/MsgEditor.vue';
import NavigationDrawer from '~/components/chat/NavigationDrawer.vue';
import Prompt from '~/components/chat/Prompt.vue';
import Welcome from '~/components/chat/Welcome.vue';
import WelcomeCard from '~/components/chat/WelcomeCard.vue';

export default {
  components: {
    ApiKeyDialog,
    ChatConversation,
    ModelDialog,
    ModelParameters,
    MsgContent,
    MsgEditor,
    NavigationDrawer,
    Prompt,
    Welcome,
    WelcomeCard,
  },
  data() {
    return {
      conversation: {
        id: null,
        messages: [],
        loadingMessages: false
      },
    };
  },
  layout: 'chatLayout',
};
</script>
