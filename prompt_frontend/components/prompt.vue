<script setup>
import { useUserStore } from '@/stores/user'
import { ref, computed } from 'vue'
import { ClipboardIcon } from "@heroicons/vue/24/outline"



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

const { prompt } = props // 解构 prompt 属性，用于访问 prompt 对象的属性


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
        await navigator.clipboard.writeText(prompt.description) // 使用解构后的 prompt 变量
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

</script>



<template>
  <div class="relative p-3 bg-gray-100 rounded-xl shadow-md flex flex-col h-full hover:shadow-lg transition-shadow">
    <div class="absolute top-3 right-3 flex items-center">
      <button
        @click="copy"
        :class="copyButtonClass"
        :disabled="copySuccess"
        class="text-sm py-2 px-2 rounded-lg flex items-center"
      >
        <ClipboardIcon class="h-4 w-5 mr-1" /><span class="text-xs ml-1">{{ copyButtonText }}</span>
      </button>
    </div>

    <div class="mb-2">
      <h3 class="text-xl font-semibold">
        {{ prompt.category.title }}
      </h3>
      <p class="text-gray-600 line-clamp-2">{{ prompt.title }}</p>
    </div>

    <div class="mb-4">
      <p class="line-clamp-4">{{ prompt.description }}</p>
    </div>

    <div class="mt-auto flex justify-between items-center">
      <p class="text-sm text-gray-500">
        {{ prompt.created_at }} | {{ prompt.company_name }}
      </p>
      <NuxtLink
        v-bind:to="'/browse/' + prompt.id"
        class="text-sm py-1 px-2 bg-blue-600 text-white rounded-lg"
      >
        Details
      </NuxtLink>
    </div>
  </div>
</template>

<style scoped>

.line-clamp-2 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
}

.line-clamp-4 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 7;
  overflow: hidden;
}

button:focus {
  outline: none;
}

.hover\:shadow-lg:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.transition-shadow {
  transition: box-shadow 0.2s ease-in-out;
}
</style>
