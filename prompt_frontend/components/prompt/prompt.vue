<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['deletePrompt'])
const props = defineProps({
    my: {
        type: [Boolean]
    },
    prompt: {
        type: [Object]
    }
})

const { prompt } = props

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

async function copy() {
    try {
        await navigator.clipboard.writeText(prompt.description)
        copySuccess.value = true;
        copyButtonText.value = '✔ 已复制!'
        setTimeout(() => {
            copySuccess.value = false
            copyButtonText.value = '复制'
        }, 2000)
    } catch (err) {
        console.error('Failed to copy text: ', err)
    }
}

const copySuccess = ref(false)
const copyButtonText = ref('复制')
const copyButtonClass = computed(() => {
    return copySuccess.value ? 'bg-green-500 text-white' : 'bg-gray-800 text-white'
})

const cardHover = ref(false)

function handleMouseOver() {
  cardHover.value = true
}

function handleMouseLeave() {
  cardHover.value = false
}
</script>

<template>
  <v-card :class="{ 'card-hover': cardHover }" outlined class="h-full relative" @mouseover="handleMouseOver" @mouseleave="handleMouseLeave">
    <v-card-title>
      <div class="flex justify-between items-center w-full">
        {{ prompt.category.title }}
      </div>
    </v-card-title>

    <div>
      <v-btn
        color="primary"
        class="copy-btn"
        @click="copy"
      >
        {{ copyButtonText }}
      </v-btn>
    </div>

    <v-card-subtitle class="text--primary text-truncate">
      {{ prompt.title }}
    </v-card-subtitle>
<!--    <v-card-text class="line-clamp-4">-->
<!--      {{ prompt.description }}-->
<!--    </v-card-text>-->

    <v-card-text class="scrollable-text">
      {{ prompt.description }}
    </v-card-text>

    <v-card-actions>
      <v-chip color="primary" text-color="white" outlined small>
        {{ prompt.created_at }} | {{ prompt.company_name }}
      </v-chip>

      <v-spacer></v-spacer>
      <router-link
          :to="'/browse/' + prompt.id"
          class="no-underline text-white bg-black"
        >
          更多...
        </router-link>
    </v-card-actions>

  </v-card>
</template>

<style scoped>
.scrollable-text {
  max-height: 10rem; /* Set a fixed height */
  overflow-y: auto; /* Enable vertical scrolling */
}

.line-clamp-4 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 7;
  overflow: hidden;
}

.copy-btn:focus {
  outline: none;
}

.copy-btn {
  position: absolute;
  top: 0;
  right: 0;
  margin-top: 0.3rem;
  margin-right: 0.3rem;
}

.text--secondary {
  position: absolute;
  left: 0;
  bottom: 0;
  margin-left: 0.3rem;
  margin-bottom: 0.3rem;
}

.card-hover {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
  transition: box-shadow 0.3s ease-in-out;
}

.no-underline {
  text-decoration: none;
}
</style>
