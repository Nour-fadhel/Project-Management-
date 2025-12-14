<!-- frontend/src/components/TaskDetailModal.vue -->
<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
    <div class="bg-white rounded-2xl shadow-xl w-full max-w-2xl max-h-[90vh] overflow-y-auto">
      <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center">
        <h3 class="text-xl font-semibold text-gray-800">Task Details</h3>
        <button @click="$emit('close')" class="text-gray-400 hover:text-gray-600">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <div class="p-6">
        <!-- Task Info -->
        <div class="mb-6">
          <div class="flex justify-between items-start mb-4">
            <div>
              <h4 class="text-lg font-bold text-gray-800 mb-2">{{ task.title }}</h4>
              <div class="flex flex-wrap gap-2">
                <span :class="statusClass" class="px-3 py-1 text-sm font-medium rounded-full">
                  {{ formatStatus(task.status) }}
                </span>
                <span :class="priorityClass" class="px-3 py-1 text-sm font-medium rounded-full">
                  {{ task.priority }}
                </span>
              </div>
            </div>

            <div class="text-right">
              <p class="text-sm text-gray-600">Project</p>
              <p class="font-medium">{{ task.project_title }}</p>
            </div>
          </div>

          <div class="bg-gray-50 rounded-lg p-4 mb-4">
            <p class="text-gray-700 whitespace-pre-line">{{ task.description || 'No description provided' }}</p>
          </div>

          <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div>
              <p class="text-sm text-gray-600">Created</p>
              <p class="font-medium">{{ formatDateTime(task.created_at) }}</p>
            </div>
            <div>
              <p class="text-sm text-gray-600">Due Date</p>
              <p :class="dueDateClass" class="font-medium">{{ formatDate(task.due_date) }}</p>
            </div>
            <div>
              <p class="text-sm text-gray-600">Estimated Hours</p>
              <p class="font-medium">{{ task.estimated_hours || '-' }}</p>
            </div>
            <div>
              <p class="text-sm text-gray-600">Actual Hours</p>
              <p class="font-medium">{{ task.actual_hours || '0' }}</p>
            </div>
          </div>
        </div>

        <!-- Status Update -->
        <div class="mb-6">
          <label class="block text-sm font-medium text-gray-700 mb-2">Update Status</label>
          <div class="flex flex-wrap gap-2">
            <button
                v-for="status in statuses"
                :key="status.value"
                @click="updateStatus(status.value)"
                :class="[status.value === task.status ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200', 'px-4 py-2 rounded-lg transition-colors']"
            >
              {{ status.label }}
            </button>
          </div>
        </div>

        <!-- Comments Section -->
        <div>
          <h5 class="text-lg font-semibold text-gray-800 mb-4">Comments</h5>

          <div class="mb-4">
            <textarea
                v-model="newComment"
                rows="3"
                placeholder="Add a comment..."
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            ></textarea>
            <button
                @click="addComment"
                class="mt-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                :disabled="!newComment.trim()"
            >
              Add Comment
            </button>
          </div>

          <div class="space-y-4" v-if="comments.length > 0">
            <div v-for="comment in comments" :key="comment.id" class="bg-gray-50 rounded-lg p-4">
              <div class="flex justify-between items-start mb-2">
                <div>
                  <p class="font-medium text-gray-800">{{ comment.user_name }}</p>
                  <p class="text-sm text-gray-500">{{ formatDateTime(comment.created_at) }}</p>
                </div>
              </div>
              <p class="text-gray-700 whitespace-pre-line">{{ comment.content }}</p>
            </div>
          </div>

          <div v-else class="text-center py-8 text-gray-500">
            No comments yet
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue'

const props = defineProps({
  task: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['close', 'update', 'add-comment'])

const comments = ref([])
const newComment = ref('')
const loading = ref(false)

const statuses = [
  { value: 'todo', label: 'To Do' },
  { value: 'in_progress', label: 'In Progress' },
  { value: 'review', label: 'Review' },
  { value: 'done', label: 'Done' },
  { value: 'blocked', label: 'Blocked' }
]

const statusClass = computed(() => {
  const classes = {
    todo: 'bg-blue-100 text-blue-800',
    in_progress: 'bg-yellow-100 text-yellow-800',
    review: 'bg-purple-100 text-purple-800',
    done: 'bg-green-100 text-green-800',
    blocked: 'bg-red-100 text-red-800'
  }
  return classes[props.task.status] || 'bg-gray-100 text-gray-800'
})

const priorityClass = computed(() => {
  const classes = {
    low: 'bg-green-100 text-green-800',
    medium: 'bg-yellow-100 text-yellow-800',
    high: 'bg-orange-100 text-orange-800',
    urgent: 'bg-red-100 text-red-800'
  }
  return classes[props.task.priority] || 'bg-gray-100 text-gray-800'
})

const dueDateClass = computed(() => {
  if (!props.task.due_date) return ''

  const now = new Date()
  const due = new Date(props.task.due_date)
  const diffDays = Math.ceil((due - now) / (1000 * 60 * 60 * 24))

  if (props.task.status === 'done') return 'text-green-600'
  if (diffDays < 0) return 'text-red-600'
  if (diffDays <= 2) return 'text-orange-600'
  return 'text-blue-600'
})

async function loadComments() {
  try {
    const token = localStorage.getItem('token')
    const response = await fetch(`http://localhost:5000/tasks/tasks/${props.task.id}/comments`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (response.ok) {
      comments.value = await response.json()
    }
  } catch (error) {
    console.error('Error loading comments:', error)
  }
}

async function updateStatus(newStatus) {
  emit('update', props.task.id, newStatus)
}

async function addComment() {
  if (!newComment.value.trim()) return

  emit('add-comment', props.task.id, newComment.value)
  newComment.value = ''

  // Reload comments after a short delay
  setTimeout(() => {
    loadComments()
  }, 500)
}

function formatDate(dateString) {
  if (!dateString) return 'No date'
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

function formatDateTime(dateTimeString) {
  if (!dateTimeString) return ''
  const date = new Date(dateTimeString)
  return date.toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

function formatStatus(status) {
  const statusMap = {
    todo: 'To Do',
    in_progress: 'In Progress',
    review: 'Review',
    done: 'Done',
    blocked: 'Blocked'
  }
  return statusMap[status] || status
}

watch(() => props.task, () => {
  if (props.task.id) {
    loadComments()
  }
}, { immediate: true })
</script>