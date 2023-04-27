<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const emit = defineEmits(['deletePrompt'])

const props = defineProps({
    my: {
        type: [Boolean]
    },
    prompt: {
        type: [Object]
    }
})

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
        alert('Content copied to clipboard')
    } catch (err) {
        console.error('Failed to copy text: ', err)
    }
}


</script>

<template>
  <div class="p-6 bg-gray-100 rounded-xl shadow-md relative">

    <div class="absolute line-clamp-1 top-1 right-1">
      <button
        @click="copy"
        :class="copyButtonClass"
        :disabled="copySuccess"
        class="text-sm py-1 px-1 rounded-lg"
      >
        {{ copyButtonText }}
      </button>
    </div>

    <div class="mb-4">
      <h3 class="line-clamp-1 text-xl font-semibold">
        {{ prompt.title }}
      </h3>
      <p class="text-gray-600">{{ prompt.category }}</p>
    </div>

    <div class="mb-4 flex-1">
      <p class="line-clamp-7">{{ prompt.description }}</p>
    </div>

    <div class="absolute bottom-4 left-4">
      <p class="inline-block mr-4">
        Posted {{ prompt.created_at }} by {{ prompt.company_name }}
      </p>
    </div>

    <div class="absolute bottom-4 right-4">
      <NuxtLink
        v-bind:to="'/browse/' + prompt.id"
        class="text-sm py-1 px-2 bg-teal-700 text-white rounded-lg"
      >
        Details
      </NuxtLink>
    </div>
  </div>
</template>

<style scoped>
.line-clamp-1 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
}

.line-clamp-7 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 7;
  overflow: hidden;
}

button:focus {
  outline: none;
}
</style>

<script>
export default {
  props: ['prompt', 'my'],
  data() {
    return {
      fullTextVisible: false,
      copySuccess: false,
      copyButtonText: 'Copy',
    };
  },
  computed: {
    copyButtonClass() {
      return this.copySuccess
        ? 'bg-green-500 text-white'
        : 'bg-indigo-500 text-white';
    },
  },
  methods: {
    toggleTextOverflow() {
      this.fullTextVisible = !this.fullTextVisible;
    },
    copy() {
      // ... 复制内容的方法
      this.copySuccess = true;
      this.copyButtonText = '✔️ Copied';

      setTimeout(() => {
        this.copySuccess = false;
        this.copyButtonText = 'Copy';
      }, 2000);
    },
    // ... 其他方法
  },
};
</script>
