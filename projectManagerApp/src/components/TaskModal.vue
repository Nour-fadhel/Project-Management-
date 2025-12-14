<template>
  <div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
    <div class="bg-white rounded-2xl w-full max-w-lg p-6">
      <h2 class="text-xl font-bold mb-4">
        {{ localTask.id ? 'Edit Task' : 'New Task' }}
      </h2>

      <form @submit.prevent="submit">
        <!-- Title -->
        <div class="mb-4">
          <label class="block text-sm font-medium">Title *</label>
          <input
              v-model="localTask.title"
              required
              class="w-full border rounded-lg px-3 py-2"
          />
        </div>

        <!-- Description -->
        <div class="mb-4">
          <label class="block text-sm font-medium">Description</label>
          <textarea
              v-model="localTask.description"
              class="w-full border rounded-lg px-3 py-2"
          ></textarea>
        </div>

        <!-- Status -->
        <div class="mb-4">
          <label class="block text-sm font-medium">Status</label>
          <select v-model="localTask.status" class="w-full border rounded-lg px-3 py-2">
            <option value="todo">To Do</option>
            <option value="in_progress">In Progress</option>
            <option value="review">Review</option>
            <option value="done">Done</option>
            <option value="blocked">Blocked</option>
          </select>
        </div>

        <!-- Priority -->
        <div class="mb-4">
          <label class="block text-sm font-medium">Priority</label>
          <select v-model="localTask.priority" class="w-full border rounded-lg px-3 py-2">
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
            <option value="urgent">Urgent</option>
          </select>
        </div>

        <!-- Due date -->
        <div class="mb-6">
          <label class="block text-sm font-medium">Due Date</label>
          <input
              type="date"
              v-model="localTask.due_date"
              class="w-full border rounded-lg px-3 py-2"
          />
          <input
              v-model="localTask.estimated_hours"
              type="number"
              step="0.5"
              placeholder="Estimated hours"
              class="w-full border rounded-lg px-3 py-2"
          />


        </div>

        <!-- Actions -->
        <div class="flex justify-end gap-3">
          <button type="button" @click="$emit('close')" class="px-4 py-2">
            Cancel
          </button>
          <button
              type="submit"
              class="px-6 py-2 bg-blue-600 text-white rounded-lg"
          >
            Save
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue'

const props = defineProps({
  task: Object
})

const emit = defineEmits(['save', 'close'])

const localTask = reactive({
  id: null,
  title: '',
  description: '',
  status: 'todo',
  priority: 'medium',
  due_date: '',
  estimated_hours: null

})

watch(
    () => props.task,
    (task) => {
      if (task) Object.assign(localTask, task)
    },
    { immediate: true }
)

function submit() {
  emit('save', { ...localTask })
}
</script>
