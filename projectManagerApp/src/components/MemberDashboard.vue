<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50 p-4 md:p-6">
    <!-- Header -->
    <header class="bg-white rounded-2xl shadow-sm p-4 md:p-6 mb-6 border border-gray-100">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div class="flex items-center space-x-4">
          <div class="w-10 h-10 md:w-12 md:h-12 bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl flex items-center justify-center">
            <svg class="w-5 h-5 md:w-6 md:h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
            </svg>
          </div>
          <div>
            <h1 class="text-xl md:text-2xl font-bold text-gray-800">Member Dashboard</h1>
            <p class="text-gray-600 text-sm">Welcome back, {{ user.name }}!</p>
          </div>
        </div>

        <div class="flex flex-wrap gap-3">
          <button
              @click="openTaskModal(null, 'todo')"
              class="flex items-center space-x-2 px-4 md:px-6 py-2 md:py-3 bg-gradient-to-r from-green-500 to-green-600 text-white rounded-xl hover:from-green-600 hover:to-green-700 transition-all duration-300 transform hover:-translate-y-0.5 shadow-lg"
          >
            <svg class="w-4 h-4 md:w-5 md:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
            </svg>
            <span class="text-sm md:text-base">New Task</span>
          </button>

          <button
              @click="handleLogout"
              class="flex items-center space-x-2 px-4 md:px-6 py-2 md:py-3 bg-gradient-to-r from-red-500 to-red-600 text-white rounded-xl hover:from-red-600 hover:to-red-700 transition-all duration-300 transform hover:-translate-y-0.5 shadow-lg"
          >
            <svg class="w-4 h-4 md:w-5 md:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
            </svg>
            <span class="text-sm md:text-base">Logout</span>
          </button>
        </div>
      </div>
    </header>

    <!-- Stats Overview -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
      <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Tasks</p>
            <p class="text-2xl md:text-3xl font-bold text-gray-800 mt-1">{{ stats.totalTasks }}</p>
          </div>
          <div class="p-2 md:p-3 bg-blue-100 rounded-xl">
            <svg class="w-5 h-5 md:w-6 md:h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">In Progress</p>
            <p class="text-2xl md:text-3xl font-bold text-gray-800 mt-1">{{ stats.inProgress }}</p>
          </div>
          <div class="p-2 md:p-3 bg-yellow-100 rounded-xl">
            <svg class="w-5 h-5 md:w-6 md:h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Completed</p>
            <p class="text-2xl md:text-3xl font-bold text-gray-800 mt-1">{{ stats.completed }}</p>
          </div>
          <div class="p-2 md:p-3 bg-green-100 rounded-xl">
            <svg class="w-5 h-5 md:w-6 md:h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Overdue</p>
            <p class="text-2xl md:text-3xl font-bold text-gray-800 mt-1">{{ stats.overdue }}</p>
          </div>
          <div class="p-2 md:p-3 bg-red-100 rounded-xl">
            <svg class="w-5 h-5 md:w-6 md:h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.732 16.5c-.77.833.192 2.5 1.732 2.5z"/>
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Project Selection -->
    <div class="mb-6">
      <div class="bg-white rounded-2xl p-4 md:p-6 shadow-sm border border-gray-100">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <div>
            <h2 class="text-lg md:text-xl font-bold text-gray-800">Task Management</h2>
            <p class="text-gray-600 text-sm mt-1">Manage your tasks in Kanban board</p>
          </div>

          <div class="flex flex-col sm:flex-row gap-3 w-full md:w-auto">


            <select
                v-model="filterStatus"
                @change="filterTasks"
                class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white"
            >
              <option value="">All Status</option>
              <option value="todo">To Do</option>
              <option value="in_progress">In Progress</option>
              <option value="review">Review</option>
              <option value="done">Done</option>
              <option value="blocked">Blocked</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <!-- Kanban Board -->
    <div class="mb-8">
      <div class="grid grid-cols-1 md:grid-cols-5 gap-4">
        <!-- To Do Column -->
        <div class="bg-blue-50 rounded-2xl p-4 border border-blue-100">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-2">
              <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
              <h3 class="font-semibold text-blue-700">To Do</h3>
              <span class="bg-blue-100 text-blue-800 text-xs font-medium px-2 py-0.5 rounded-full">
                {{ columns.todo.length }}
              </span>
            </div>
            <button
                @click="openTaskModal(null, 'todo')"
                class="p-1 text-blue-600 hover:text-blue-700"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
              </svg>
            </button>
          </div>

          <draggable
              :list="columns.todo"
              :group="{ name: 'tasks', pull: true, put: true }"
              @end="onDragEnd"
              item-key="id"
              class="min-h-[200px] space-y-3"
              :data-status="'todo'"
          >
            <template #item="{ element }">
              <TaskCard :task="element" @click="openTaskDetail(element)" />
            </template>
          </draggable>
        </div>

        <!-- In Progress Column -->
        <div class="bg-yellow-50 rounded-2xl p-4 border border-yellow-100">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-2">
              <div class="w-3 h-3 bg-yellow-500 rounded-full"></div>
              <h3 class="font-semibold text-yellow-700">In Progress</h3>
              <span class="bg-yellow-100 text-yellow-800 text-xs font-medium px-2 py-0.5 rounded-full">
                {{ columns.in_progress.length }}
              </span>
            </div>
          </div>

          <draggable
              :list="columns.in_progress"
              :group="{ name: 'tasks', pull: true, put: true }"
              @end="onDragEnd"
              item-key="id"
              class="min-h-[200px] space-y-3"
              :data-status="'in_progress'"
          >
            <template #item="{ element }">
              <TaskCard :task="element" @click="openTaskDetail(element)" />
            </template>
          </draggable>
        </div>

        <!-- Review Column -->
        <div class="bg-purple-50 rounded-2xl p-4 border border-purple-100">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-2">
              <div class="w-3 h-3 bg-purple-500 rounded-full"></div>
              <h3 class="font-semibold text-purple-700">Review</h3>
              <span class="bg-purple-100 text-purple-800 text-xs font-medium px-2 py-0.5 rounded-full">
                {{ columns.review.length }}
              </span>
            </div>
          </div>

          <draggable
              :list="columns.review"
              :group="{ name: 'tasks', pull: true, put: true }"
              @end="onDragEnd"
              item-key="id"
              class="min-h-[200px] space-y-3"
              :data-status="'review'"
          >
            <template #item="{ element }">
              <TaskCard :task="element" @click="openTaskDetail(element)" />
            </template>
          </draggable>
        </div>

        <!-- Done Column -->
        <div class="bg-green-50 rounded-2xl p-4 border border-green-100">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-2">
              <div class="w-3 h-3 bg-green-500 rounded-full"></div>
              <h3 class="font-semibold text-green-700">Done</h3>
              <span class="bg-green-100 text-green-800 text-xs font-medium px-2 py-0.5 rounded-full">
                {{ columns.done.length }}
              </span>
            </div>
          </div>

          <draggable
              :list="columns.done"
              :group="{ name: 'tasks', pull: true, put: true }"
              @end="onDragEnd"
              item-key="id"
              class="min-h-[200px] space-y-3"
              :data-status="'done'"
          >
            <template #item="{ element }">
              <TaskCard :task="element" @click="openTaskDetail(element)" />
            </template>
          </draggable>
        </div>

        <!-- Blocked Column -->
        <div class="bg-red-50 rounded-2xl p-4 border border-red-100">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-2">
              <div class="w-3 h-3 bg-red-500 rounded-full"></div>
              <h3 class="font-semibold text-red-700">Blocked</h3>
              <span class="bg-red-100 text-red-800 text-xs font-medium px-2 py-0.5 rounded-full">
                {{ columns.blocked.length }}
              </span>
            </div>
          </div>

          <draggable
              :list="columns.blocked"
              :group="{ name: 'tasks', pull: true, put: true }"
              @end="onDragEnd"
              item-key="id"
              class="min-h-[200px] space-y-3"
              :data-status="'blocked'"
          >
            <template #item="{ element }">
              <TaskCard :task="element" @click="openTaskDetail(element)" />
            </template>
          </draggable>
        </div>
      </div>
    </div>

    <!-- Task List View -->
    <div class="mb-8">
      <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="px-4 md:px-6 py-4 border-b border-gray-200">
          <h3 class="text-lg font-semibold text-gray-800">All Tasks</h3>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50">
            <tr>
              <th class="px-4 md:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Task</th>
              <th class="px-4 md:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Project</th>
              <th class="px-4 md:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Priority</th>
              <th class="px-4 md:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Due Date</th>
              <th class="px-4 md:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
              <th class="px-4 md:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="task in allTasks" :key="task.id">
              <td class="px-4 md:px-6 py-4">
                <div>
                  <div class="font-medium text-gray-900">{{ task.title }}</div>
                  <div class="text-sm text-gray-500 truncate max-w-xs">{{ task.description }}</div>
                </div>
              </td>
              <td class="px-4 md:px-6 py-4 text-sm text-gray-900">{{ task.project_title }}</td>
              <td class="px-4 md:px-6 py-4">
                  <span :class="priorityClass(task.priority)" class="px-2 py-1 text-xs font-medium rounded-full">
                    {{ task.priority }}
                  </span>
              </td>
              <td class="px-4 md:px-6 py-4 text-sm">
                  <span :class="dueDateClass(task.due_date, task.status)" class="px-2 py-1 text-xs font-medium rounded-full">
                    {{ formatDate(task.due_date) }}
                  </span>
              </td>
              <td class="px-4 md:px-6 py-4">
                  <span :class="statusClass(task.status)" class="px-2 py-1 text-xs font-medium rounded-full">
                    {{ formatStatus(task.status) }}
                  </span>
              </td>
              <td class="px-4 md:px-6 py-4 text-sm font-medium">
                <button @click="openTaskDetail(task)" class="text-blue-600 hover:text-blue-900 mr-3">View</button>
                <button @click="openTaskModal(task)" class="text-green-600 hover:text-green-900 mr-3">Edit</button>
                <button @click="deleteTask(task.id)" class="text-red-600 hover:text-red-900">Delete</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Task Modal -->
    <TaskModal
        v-if="showTaskModal"
        :task="currentTask"
        :projects="projects"
        @close="closeTaskModal"
        @save="saveTask"
    />

    <!-- Task Detail Modal -->
    <TaskDetailModal
        v-if="showTaskDetail"
        :task="selectedTask"
        @close="closeTaskDetail"
        @update="updateTaskStatus"
        @add-comment="addComment"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { VueDraggableNext as draggable } from 'vuedraggable'
import TaskCard from '../components/TaskCard.vue'
import TaskModal from '../components/TaskModal.vue'
import TaskDetailModal from '../components/TaskDetailModal.vue'

const router = useRouter()

// User data
const user = ref({
  name: localStorage.getItem('userName') || 'Member',
  role: localStorage.getItem('userRole') || 'member'
})

// State
const projects = ref([])
const allTasks = ref([])
const selectedProject = ref('')
const filterStatus = ref('')

// Stats
const stats = ref({
  totalTasks: 0,
  inProgress: 0,
  completed: 0,
  overdue: 0
})

// Kanban columns
const columns = ref({
  todo: [],
  in_progress: [],
  review: [],
  done: [],
  blocked: []
})

// Modals
const showTaskModal = ref(false)
const showTaskDetail = ref(false)
const currentTask = ref(null)
const selectedTask = ref(null)

// Methods

function statusClass(status) {
  const classes = {
    todo: 'bg-blue-100 text-blue-800',
    in_progress: 'bg-yellow-100 text-yellow-800',
    review: 'bg-purple-100 text-purple-800',
    done: 'bg-green-100 text-green-800',
    blocked: 'bg-red-100 text-red-800'
  }

  return classes[status] || 'bg-gray-100 text-gray-800'
}

function dueDateClass(dueDate, status) {
  if (!dueDate) return 'bg-gray-100 text-gray-800'

  if (status === 'done') {
    return 'bg-green-100 text-green-800'
  }

  const now = new Date()
  const due = new Date(dueDate)

  if (due < now) {
    return 'bg-red-100 text-red-800'
  }

  return 'bg-blue-100 text-blue-800'
}

function formatDate(date) {
  if (!date) return '—'

  const d = new Date(date)
  if (isNaN(d.getTime())) return '—'

  return d.toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}


async function loadProjects() {
  try {
    const token = localStorage.getItem('token')
    const response = await fetch('http://localhost:5000/projects', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (response.ok) {
      projects.value = await response.json()
    }
  } catch (error) {
    console.error('Error loading projects:', error)
  }
}

async function loadMyTasks() {
  try {
    const token = localStorage.getItem('token')
    const response = await fetch('http://localhost:5000/tasks/my-tasks', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (response.ok) {
      allTasks.value = await response.json()
      organizeTasksIntoColumns()
      updateStats()
    }
  } catch (error) {
    console.error('Error loading tasks:', error)
  }
}

async function loadProjectTasks() {
  if (!selectedProject.value) {
    loadMyTasks()
    return
  }

  try {
    const token = localStorage.getItem('token')
    const response = await fetch(`http://localhost:5000/tasks/projects/${selectedProject.value}/tasks`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (response.ok) {
      allTasks.value = await response.json()
      organizeTasksIntoColumns()
      updateStats()
    }
  } catch (error) {
    console.error('Error loading project tasks:', error)
  }
}

function organizeTasksIntoColumns() {
  columns.value = {
    todo: [],
    in_progress: [],
    review: [],
    done: [],
    blocked: []
  }

  allTasks.value.forEach(task => {
    if (columns.value[task.status]) {
      columns.value[task.status].push(task)
    }
  })
}

function updateStats() {
  const now = new Date()

  stats.value = {
    totalTasks: allTasks.value.length,
    inProgress: allTasks.value.filter(t => t.status === 'in_progress').length,
    completed: allTasks.value.filter(t => t.status === 'done').length,
    overdue: allTasks.value.filter(t => {
      if (!t.due_date || t.status === 'done') return false
      const dueDate = new Date(t.due_date)
      return dueDate < now
    }).length
  }
}

async function onDragEnd(event) {
  const { to, item } = event
  const taskId = item.getAttribute('data-task-id') || event.item._underlying_vm_?.id
  const newStatus = to.getAttribute('data-status')

  if (!taskId || !newStatus) return

  try {
    const token = localStorage.getItem('token')
    const response = await fetch(`http://localhost:5000/tasks/tasks/${taskId}/status`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ status: newStatus })
    })

    if (!response.ok) {
      throw new Error('Failed to update task status')
    }

    updateStats()
  } catch (error) {
    console.error('Error updating task status:', error)
    alert('Failed to update task status')
    if (selectedProject.value) {
      await loadProjectTasks()
    } else {
      await loadMyTasks()
    }
  }
}

async function saveTask(taskData) {
  try {
    const token = localStorage.getItem('token');

    // Remove any project_id that might be sent
    delete taskData.project_id;

    // Get the correct endpoint
    const url = taskData.id
        ? `http://localhost:5000/tasks/tasks/${taskData.id}`
        : `http://localhost:5000/tasks/my-project/tasks`;

    const method = taskData.id ? 'PUT' : 'POST';

    console.log('Saving task:', taskData);
    console.log('URL:', url);
    console.log('Method:', method);

    const response = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(taskData)
    });

    const result = await response.json();

    if (!response.ok) {
      console.error('Error response:', result);
      throw new Error(result.message || 'Failed to save task');
    }

    alert(taskData.id ? 'Task updated!' : 'Task created!');
    closeTaskModal();

    // Reload tasks
    await loadMyTasks();

  } catch (error) {
    console.error('Error saving task:', error);
    alert(error.message);
  }
}

async function deleteTask(taskId) {
  if (!confirm('Are you sure you want to delete this task?')) return

  try {
    const token = localStorage.getItem('token')
    const response = await fetch(`http://localhost:5000/tasks/tasks/${taskId}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (response.ok) {
      alert('Task deleted successfully!')

      if (selectedProject.value) {
        await loadProjectTasks()
      } else {
        await loadMyTasks()
      }
    }
  } catch (error) {
    console.error('Error deleting task:', error)
    alert('Failed to delete task')
  }
}

async function updateTaskStatus(taskId, status) {
  try {
    const token = localStorage.getItem('token')
    const response = await fetch(`http://localhost:5000/tasks/tasks/${taskId}/status`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ status })
    })

    if (response.ok) {
      if (selectedProject.value) {
        await loadProjectTasks()
      } else {
        await loadMyTasks()
      }
    }
  } catch (error) {
    console.error('Error updating task status:', error)
  }
}

async function addComment(taskId, content) {
  try {
    const token = localStorage.getItem('token')
    const response = await fetch(`http://localhost:5000/tasks/tasks/${taskId}/comments`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ content })
    })

    if (response.ok) {
      alert('Comment added successfully!')
    }
  } catch (error) {
    console.error('Error adding comment:', error)
    alert('Failed to add comment')
  }
}

function openTaskModal(task = null, defaultStatus = 'todo') {
  currentTask.value = task || {
    title: '',
    description: '',
    status: defaultStatus,
    priority: 'medium',
    due_date: '',
    estimated_hours: null
  }

  showTaskModal.value = true
}



function closeTaskModal() {
  showTaskModal.value = false
  currentTask.value = null
}

function openTaskDetail(task) {
  selectedTask.value = task
  showTaskDetail.value = true
}

function closeTaskDetail() {
  showTaskDetail.value = false
  selectedTask.value = null
}

function filterTasks() {
  const filtered = filterStatus.value
      ? allTasks.value.filter(t => t.status === filterStatus.value)
      : allTasks.value

  columns.value = {
    todo: [],
    in_progress: [],
    review: [],
    done: [],
    blocked: []
  }

  filtered.forEach(task => {
    columns.value[task.status]?.push(task)
  })
}


function priorityClass(priority) {
  const classes = {
    low: 'bg-green-100 text-green-800',
    medium: 'bg-yellow-100 text-yellow-800',
    high: 'bg-orange-100 text-orange-800',
    urgent: 'bg-red-100 text-red-800'
  }
  return classes[priority] || 'bg-gray-100 text-gray-800'
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

function handleLogout() {
  localStorage.clear()
  router.push('/login')
}

// Lifecycle
onMounted(() => {
  loadProjects()
  loadMyTasks()
})
</script>

<style scoped>
/* Add any custom styles here */
</style>