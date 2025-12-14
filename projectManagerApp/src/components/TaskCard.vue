
<template>
  <div
      @click="$emit('click', task)"
      class="bg-white rounded-lg p-3 shadow-sm border border-gray-200 hover:shadow-md transition-shadow cursor-pointer"
  >
    <div class="flex justify-between items-start mb-2">
      <h4 class="font-medium text-gray-800 text-sm line-clamp-2">{{ task.title }}</h4>
      <span :class="priorityBadgeClass" class="text-xs font-medium px-1.5 py-0.5 rounded">
        {{ task.priority.charAt(0).toUpperCase() }}
      </span>
    </div>

    <p class="text-gray-600 text-xs mb-3 line-clamp-2">{{ task.description || 'No description' }}</p>

    <div class="flex justify-between items-center text-xs text-gray-500">
      <div class="flex items-center">
        <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        <span>{{ formatDate(task.due_date) }}</span>
      </div>

      <div class="flex items-center">
        <div class="w-2 h-2 rounded-full bg-blue-500 mr-1"></div>
        <span>{{ task.project_title?.substring(0, 10) }}...</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  task: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['click'])

const priorityBadgeClass = computed(() => {
  const classes = {
    low: 'bg-green-100 text-green-800',
    medium: 'bg-yellow-100 text-yellow-800',
    high: 'bg-orange-100 text-orange-800',
    urgent: 'bg-red-100 text-red-800'
  }
  return classes[props.task.priority] || 'bg-gray-100 text-gray-800'
})

function formatDate(dateString) {
  if (!dateString) return 'No date'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}
</script>