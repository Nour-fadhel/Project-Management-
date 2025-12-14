<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-4 md:p-6">
    <!-- Floating Background Elements -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute -top-40 -right-40 w-80 h-80 bg-gradient-to-r from-blue-500/10 to-purple-500/10 rounded-full blur-3xl"></div>
      <div class="absolute -bottom-40 -left-40 w-80 h-80 bg-gradient-to-r from-emerald-500/10 to-cyan-500/10 rounded-full blur-3xl"></div>
    </div>

    <!-- Animated Header -->
    <div class="relative mb-8">
      <div class="bg-gradient-to-r from-white/90 to-white/80 backdrop-blur-xl rounded-2xl shadow-2xl p-6 border border-white/30">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <div class="flex items-center space-x-4">
            <div class="relative">
              <div class="w-14 h-14 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-500/30">
                <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                </svg>
              </div>
              <div class="absolute -top-1 -right-1 w-5 h-5 bg-emerald-500 rounded-full border-2 border-white"></div>
            </div>
            <div>
              <h1 class="text-3xl md:text-4xl font-bold bg-gradient-to-r from-gray-800 to-gray-900 bg-clip-text text-transparent">
                Project Tasks Dashboard
              </h1>
              <p class="text-gray-600 mt-1 flex items-center">
                <span class="w-2 h-2 bg-emerald-500 rounded-full mr-2 animate-pulse"></span>
                Real-time task management & progress tracking
              </p>
            </div>
          </div>

          <!-- Animated Stats -->
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3 animate-slide-up">
            <div class="bg-gradient-to-br from-blue-50 to-blue-100/50 rounded-xl p-3 border border-blue-200/50 backdrop-blur-sm shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
              <p class="text-xs font-semibold text-blue-700/80 uppercase tracking-wider">Total Tasks</p>
              <div class="flex items-center justify-between mt-1">
                <p class="text-2xl font-bold text-blue-900">{{ tasks.length }}</p>
                <svg class="w-5 h-5 text-blue-600/70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                </svg>
              </div>
            </div>
            <div class="bg-gradient-to-br from-emerald-50 to-emerald-100/50 rounded-xl p-3 border border-emerald-200/50 backdrop-blur-sm shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
              <p class="text-xs font-semibold text-emerald-700/80 uppercase tracking-wider">Completed</p>
              <div class="flex items-center justify-between mt-1">
                <p class="text-2xl font-bold text-emerald-900">{{ completedTasks }}</p>
                <svg class="w-5 h-5 text-emerald-600/70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
            </div>
            <div class="bg-gradient-to-br from-amber-50 to-amber-100/50 rounded-xl p-3 border border-amber-200/50 backdrop-blur-sm shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
              <p class="text-xs font-semibold text-amber-700/80 uppercase tracking-wider">In Progress</p>
              <div class="flex items-center justify-between mt-1">
                <p class="text-2xl font-bold text-amber-900">{{ inProgressTasks }}</p>
                <svg class="w-5 h-5 text-amber-600/70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
            </div>
            <div class="bg-gradient-to-br from-purple-50 to-purple-100/50 rounded-xl p-3 border border-purple-200/50 backdrop-blur-sm shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
              <p class="text-xs font-semibold text-purple-700/80 uppercase tracking-wider">Total Hours</p>
              <div class="flex items-center justify-between mt-1">
                <p class="text-2xl font-bold text-purple-900">{{ totalEstimatedHours }}h</p>
                <svg class="w-5 h-5 text-purple-600/70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="relative grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Left Column: Tasks Table -->
      <div class="lg:col-span-2">
        <!-- Search and Filter Bar -->
        <div class="bg-gradient-to-r from-white/90 to-white/80 backdrop-blur-xl rounded-2xl shadow-xl p-4 mb-4 border border-white/30">
          <div class="flex flex-col md:flex-row gap-4">
            <div class="flex-1 relative">
              <svg class="w-5 h-5 absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
              </svg>
              <input
                  v-model="searchQuery"
                  @input="filterTasks"
                  type="text"
                  placeholder="Search tasks by name, description, or assignee..."
                  class="w-full pl-12 pr-4 py-3 bg-white/50 border border-gray-200/50 rounded-xl focus:ring-2 focus:ring-indigo-500/30 focus:border-indigo-500 transition-all duration-300"
              />
            </div>
            <div class="flex gap-3">
              <select
                  v-model="filterStatus"
                  @change="filterTasks"
                  class="px-4 py-3 bg-white/50 border border-gray-200/50 rounded-xl focus:ring-2 focus:ring-indigo-500/30 focus:border-indigo-500 transition-all duration-300"
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

        <!-- Tasks Table Container -->
        <div class="bg-gradient-to-br from-white/90 to-white/80 backdrop-blur-xl rounded-2xl shadow-2xl overflow-hidden border border-white/30 animate-fade-in">
          <!-- Table Header -->
          <div class="px-6 py-4 bg-gradient-to-r from-gray-50/50 to-gray-100/50 border-b border-gray-200/30">
            <div class="flex justify-between items-center">
              <h2 class="text-xl font-bold bg-gradient-to-r from-gray-700 to-gray-900 bg-clip-text text-transparent">
                Project Tasks <span class="text-gray-500">({{ filteredTasks.length }})</span>
              </h2>
              <div class="flex items-center space-x-2 text-sm text-gray-600">
                <span class="w-2 h-2 bg-emerald-500 rounded-full"></span>
                <span>Last updated: {{ lastUpdated }}</span>
              </div>
            </div>
          </div>

          <!-- Table -->
          <div class="overflow-x-auto">
            <table class="w-full">
              <thead>
              <tr class="bg-gradient-to-r from-gray-50/80 to-gray-100/80">
                <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider">
                  <div class="flex items-center group cursor-pointer" @click="sortBy('title')">
                    Task Details
                    <svg class="w-4 h-4 ml-2 text-gray-400 group-hover:text-gray-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4"/>
                    </svg>
                  </div>
                </th>
                <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider">
                  <div class="flex items-center group cursor-pointer" @click="sortBy('status')">
                    Status
                    <svg class="w-4 h-4 ml-2 text-gray-400 group-hover:text-gray-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4"/>
                    </svg>
                  </div>
                </th>
                <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider">
                  <div class="flex items-center group cursor-pointer" @click="sortBy('estimated_hours')">
                    Time
                    <svg class="w-4 h-4 ml-2 text-gray-400 group-hover:text-gray-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4"/>
                    </svg>
                  </div>
                </th>
                <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider">Assignee</th>
              </tr>
              </thead>
              <tbody class="divide-y divide-gray-200/30">
              <tr
                  v-for="task in filteredTasks"
                  :key="task.id"
                  @click="openTaskFeedback(task)"
                  class="cursor-pointer hover:bg-indigo-50 transition-all"
              >

              <td class="px-6 py-4">
                  <div class="flex items-start space-x-3">
                    <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-blue-100 to-indigo-100 flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
                      <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                      </svg>
                    </div>
                    <div>
                      <h4 class="font-semibold text-gray-900 group-hover:text-indigo-600 transition-colors">
                        {{ task.title }}
                      </h4>
                      <p class="text-sm text-gray-600 mt-1 line-clamp-2">{{ task.description || 'No description provided' }}</p>
                      <div class="flex items-center mt-2">

                        <span class="text-xs text-gray-500 ml-2">
                            {{ formatDate(task.created_at) }}
                          </span>
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4">
                  <div class="flex flex-col items-start">
                      <span :class="statusClass(task.status)" class="px-3 py-1.5 rounded-full text-sm font-medium mb-1">
                        {{ formatStatus(task.status) }}
                      </span>
                    <div v-if="task.due_date" class="text-xs text-gray-500 flex items-center">
                      <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                      </svg>
                      Due {{ formatDate(task.due_date) }}
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center space-x-3">
                    <div class="relative">
                      <svg class="w-10 h-10 text-gray-200" viewBox="0 0 36 36">
                        <path
                            d="M18 2.0845
                              a 15.9155 15.9155 0 0 1 0 31.831
                              a 15.9155 15.9155 0 0 1 0 -31.831"
                            fill="none"
                            stroke="currentColor"
                            stroke-width="3"
                            stroke-dasharray="100, 100"
                        />
                        <path
                            d="M18 2.0845
                              a 15.9155 15.9155 0 0 1 0 31.831
                              a 15.9155 15.9155 0 0 1 0 -31.831"
                            fill="none"
                            :stroke="getTimeColor(task)"
                            stroke-width="3"
                            :stroke-dasharray="getTimeProgress(task)"
                            stroke-linecap="round"
                            class="transition-all duration-500"
                        />
                      </svg>
                      <span class="absolute inset-0 flex items-center justify-center text-xs font-bold" :class="getTimeTextColor(task)">
                          {{ task.estimated_hours || 0 }}h
                        </span>
                    </div>
                    <div>
                      <div class="text-sm font-medium text-gray-900">{{ task.estimated_hours || 0 }}h estimated</div>
                      <div class="text-xs text-gray-500">{{ task.actual_hours || 0 }}h actual</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center space-x-3">
                    <div class="relative">
                      <div class="w-10 h-10 rounded-full bg-gradient-to-r from-blue-400 to-indigo-600 flex items-center justify-center text-white text-sm font-semibold shadow-lg">
                        {{ task.assigned_to ?? '?' }}
                      </div>

                      <div>
                        <div class="font-medium text-gray-900">
                         Member name : {{ task.assigned_to ?? 'Unassigned' }}
                        </div>
                        <div class="text-xs text-gray-500">
                          Member
                        </div>
                      </div>

                    </div>
                  </div>
                </td>

              </tr>
              </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="filteredTasks.length === 0" class="text-center py-16">
              <div class="w-24 h-24 mx-auto mb-6">
                <svg class="w-full h-full text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-700 mb-2">No tasks found</h3>
              <p class="text-gray-500 mb-6">Try adjusting your search or create a new task</p>
              <button @click="createTask" class="px-6 py-3 bg-gradient-to-r from-indigo-500 to-purple-600 text-white rounded-xl hover:shadow-lg hover:shadow-indigo-500/30 transition-all duration-300">
                Create New Task
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Analytics -->
      <div class="space-y-6">
        <!-- Burndown Chart Card -->
        <div class="bg-gradient-to-br from-white/90 to-white/80 backdrop-blur-xl rounded-2xl shadow-2xl p-6 border border-white/30 animate-slide-up" style="animation-delay: 0.1s">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h3 class="text-xl font-bold bg-gradient-to-r from-gray-700 to-gray-900 bg-clip-text text-transparent">
                Burndown Analysis
              </h3>
              <p class="text-gray-600 text-sm">Project progress tracking</p>
            </div>
            <div class="p-3 bg-gradient-to-r from-indigo-100 to-purple-100 rounded-xl">
              <svg class="w-6 h-6 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"/>
              </svg>
            </div>
          </div>

          <div class="h-64 mb-6">
            <canvas ref="burndownChart"></canvas>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="bg-gradient-to-br from-emerald-50 to-emerald-100/50 rounded-xl p-4 border border-emerald-200/50">
              <div class="flex items-center">
                <div class="w-12 h-12 bg-gradient-to-r from-emerald-500 to-teal-600 rounded-lg flex items-center justify-center mr-3 shadow-lg shadow-emerald-500/30">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-semibold text-emerald-700/80 uppercase tracking-wider">Completed</p>
                  <p class="text-2xl font-bold text-emerald-900">{{ completedHours }}h</p>
                  <p class="text-xs text-emerald-600 mt-1">{{ Math.round((completedHours / totalEstimatedHours) * 100) || 0 }}% of total</p>
                </div>
              </div>
            </div>
            <div class="bg-gradient-to-br from-blue-50 to-blue-100/50 rounded-xl p-4 border border-blue-200/50">
              <div class="flex items-center">
                <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center mr-3 shadow-lg shadow-blue-500/30">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-semibold text-blue-700/80 uppercase tracking-wider">Remaining</p>
                  <p class="text-2xl font-bold text-blue-900">{{ totalEstimatedHours - completedHours }}h</p>
                  <p class="text-xs text-blue-600 mt-1">{{ Math.round(((totalEstimatedHours - completedHours) / totalEstimatedHours) * 100) || 0 }}% remaining</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Status Distribution Card -->
        <div class="bg-gradient-to-br from-white/90 to-white/80 backdrop-blur-xl rounded-2xl shadow-2xl p-6 border border-white/30 animate-slide-up" style="animation-delay: 0.2s">
          <h3 class="text-xl font-bold bg-gradient-to-r from-gray-700 to-gray-900 bg-clip-text text-transparent mb-6">
            Status Distribution
          </h3>

          <div class="space-y-4 mb-6">
            <div v-for="status in statusStats" :key="status.name" class="flex items-center justify-between group cursor-pointer hover:bg-white/50 p-2 rounded-lg transition-all duration-300">
              <div class="flex items-center">
                <div class="w-8 h-8 rounded-lg flex items-center justify-center mr-3" :class="status.iconBg">
                  <svg class="w-4 h-4" :class="status.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="status.iconPath"/>
                  </svg>
                </div>
                <div>
                  <span class="text-sm font-medium text-gray-700">{{ status.label }}</span>
                  <div class="flex items-center">
                    <div class="w-24 h-1.5 bg-gray-200 rounded-full overflow-hidden mr-2">
                      <div class="h-full rounded-full transition-all duration-500" :style="{ width: status.percentage + '%' }" :class="status.color"></div>
                    </div>
                    <span class="text-xs text-gray-500">{{ status.percentage }}%</span>
                  </div>
                </div>
              </div>
              <span class="font-bold text-gray-900">{{ status.count }}</span>
            </div>
          </div>

          <div class="pt-6 border-t border-gray-200/30">
            <div class="flex justify-between text-sm mb-2">
              <span class="text-gray-600">Overall Progress</span>
              <span class="font-bold text-gray-900">{{ completionPercentage }}% complete</span>
            </div>
            <div class="h-2 bg-gradient-to-r from-gray-200 to-gray-300 rounded-full overflow-hidden">
              <div
                  class="h-full bg-gradient-to-r from-emerald-400 via-emerald-500 to-emerald-600 rounded-full transition-all duration-1000 ease-out"
                  :style="{ width: completionPercentage + '%' }"
              ></div>
            </div>
          </div>
        </div>



        <!-- Task Deadlines Calendar -->
        <div
            class="bg-gradient-to-br from-white/90 to-white/80 backdrop-blur-xl
         rounded-2xl shadow-2xl p-6 border border-white/30
         animate-slide-up"
            style="animation-delay: 0.3s"
        >
          <div class="flex items-center justify-between mb-4">
            <div>
              <h3 class="text-xl font-bold bg-gradient-to-r from-gray-700 to-gray-900 bg-clip-text text-transparent">
                Task Deadlines
              </h3>
              <p class="text-gray-600 text-sm">
                Upcoming task due dates
              </p>
            </div>

            <div class="p-3 bg-gradient-to-r from-indigo-100 to-purple-100 rounded-xl">
              📅
            </div>
          </div>

          <FullCalendar
              :plugins="[dayGridPlugin, interactionPlugin]"
              initialView="dayGridMonth"
              :events="calendarEvents"
              height="auto"
              :headerToolbar="{
    left: 'prev,next',
    center: 'title'
  }"
          />

        </div>



      </div>
    </div>
  </div>
  <!-- Feedback Modal -->
  <div v-if="showFeedbackModal" class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center">
    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-2xl p-6 relative">

      <!-- Header -->
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-xl font-bold">
          Task Feedback – {{ selectedTask?.title }}
        </h3>
        <button @click="closeFeedbackModal" class="text-gray-400 hover:text-gray-600">
          ✕
        </button>
      </div>

      <!-- Overall Sentiment -->
      <div class="mb-4">
      <span
          class="px-4 py-2 rounded-full text-sm font-semibold"
          :class="sentimentBadge(overallSentiment)"
      >
        Overall Sentiment: {{ overallSentiment }}
      </span>
      </div>

      <!-- Comments -->
      <div class="space-y-3 max-h-96 overflow-y-auto">
        <div
            v-for="comment in taskComments"
            :key="comment.id"
            class="p-4 rounded-xl border flex justify-between items-start"
        >
          <p class="text-gray-800">{{ comment.content }}</p>

          <span
              class="ml-4 px-3 py-1 text-xs font-semibold rounded-full"
              :class="sentimentBadge(comment.sentiment)"
          >
          {{ comment.sentiment }}
        </span>
        </div>


      </div>
    </div>
  </div>

</template>

<script>
import Chart from "chart.js/auto";
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";
components: {
  FullCalendar
}
export default {
  data() {
    return {
      tasks: [],
      filteredTasks: [],
      searchQuery: '',
      filterStatus: '',
      sortField: 'created_at',
      sortDirection: 'desc',
      showFeedbackModal: false,
      selectedTask: null,
      taskComments: [],
      overallSentiment: "Neutral",
      FullCalendar,
      chart: null,
      lastUpdated: new Date().toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
      })
    };
  },

  computed: {
    completedTasks() {
      return this.tasks.filter(t => t.status === "done").length;
    },

    inProgressTasks() {
      return this.tasks.filter(t => t.status === "in_progress").length;
    },

    totalEstimatedHours() {
      return this.tasks.reduce((sum, t) => sum + (t.estimated_hours || 0), 0);
    },

    completedHours() {
      return this.tasks
          .filter(t => t.status === "done")
          .reduce((sum, t) => sum + (t.estimated_hours || 0), 0);
    },

    completionPercentage() {
      if (this.totalEstimatedHours === 0) return 0;
      return Math.round((this.completedHours / this.totalEstimatedHours) * 100);
    },

    blockedTasks() {
      return this.tasks.filter(t => t.status === "blocked").length;
    },

    efficiencyRate() {
      const completedOnTime = this.tasks.filter(t =>
          t.status === "done" &&
          t.due_date &&
          new Date(t.completed_at || t.updated_at) <= new Date(t.due_date)
      ).length;

      const totalDone = this.completedTasks;
      return totalDone > 0 ? Math.round((completedOnTime / totalDone) * 100) : 0;
    },

    fastestTask() {
      const doneTasks = this.tasks.filter(t => t.status === "done");
      if (doneTasks.length === 0) return null;

      return doneTasks.reduce((fastest, task) => {
        const taskDuration = task.actual_hours || task.estimated_hours || 0;
        const fastestDuration = fastest.actual_hours || fastest.estimated_hours || 0;
        return taskDuration < fastestDuration ? task : fastest;
      });
    },

    statusStats() {
      const statusConfig = {
        'todo': {
          label: 'To Do',
          color: 'bg-blue-500',
          iconBg: 'bg-blue-100',
          iconColor: 'text-blue-600',
          iconPath: 'M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2'
        },
        'in_progress': {
          label: 'In Progress',
          color: 'bg-amber-500',
          iconBg: 'bg-amber-100',
          iconColor: 'text-amber-600',
          iconPath: 'M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z'
        },
        'review': {
          label: 'Review',
          color: 'bg-purple-500',
          iconBg: 'bg-purple-100',
          iconColor: 'text-purple-600',
          iconPath: 'M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z'
        },
        'done': {
          label: 'Done',
          color: 'bg-emerald-500',
          iconBg: 'bg-emerald-100',
          iconColor: 'text-emerald-600',
          iconPath: 'M5 13l4 4L19 7'
        },
        'blocked': {
          label: 'Blocked',
          color: 'bg-rose-500',
          iconBg: 'bg-rose-100',
          iconColor: 'text-rose-600',
          iconPath: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.732 16.5c-.77.833.192 2.5 1.732 2.5z'
        }
      };

      return Object.entries(statusConfig).map(([status, config]) => {
        const count = this.tasks.filter(t => t.status === status).length;
        const percentage = this.tasks.length > 0 ? Math.round((count / this.tasks.length) * 100) : 0;

        return {
          name: status,
          ...config,
          count: count,
          percentage: percentage
        };
      });
    },
    calendarEvents() {
      return this.tasks
          .filter(t => t.due_date)
          .map(task => ({
            title: task.title,
            date: task.due_date,
            backgroundColor: this.getCalendarColor(task),
            borderColor: "transparent"
          }));
    },
  },

  async mounted() {
    await this.loadTasks();
    this.filteredTasks = [...this.tasks];
    this.renderBurndown();

    // Auto-refresh every 30 seconds
    setInterval(async () => {
      await this.loadTasks();
    }, 30000);
  },

  methods: {

    formatDate(dateString) {
      if (!dateString) return "—";

      const date = new Date(dateString);

      if (isNaN(date.getTime())) return "—";

      return date.toLocaleDateString("en-US", {
        year: "numeric",
        month: "short",
        day: "numeric"
      });
    },

    getTimeColor(task) {
      if (!task.due_date) return '#94a3b8'; // gray

      const dueDate = new Date(task.due_date);
      const now = new Date();
      const diffDays = Math.ceil((dueDate - now) / (1000 * 60 * 60 * 24));

      if (task.status === 'done') return '#10b981'; // green
      if (diffDays < 0) return '#ef4444'; // red (overdue)
      if (diffDays <= 2) return '#f59e0b'; // amber (urgent)
      return '#3b82f6'; // blue (on track)
    },

    getTimeTextColor(task) {
      const color = this.getTimeColor(task);

      if (color === '#10b981') return 'text-emerald-600';
      if (color === '#ef4444') return 'text-rose-600';
      if (color === '#f59e0b') return 'text-amber-600';
      return 'text-blue-600';
    },

    getTimeProgress(task) {
      const estimated = task.estimated_hours || 1;
      const actual = task.actual_hours || 0;

      const percentage = Math.min(100, Math.round((actual / estimated) * 100));

      // SVG stroke-dasharray format: "value, total"
      return `${percentage}, 100`;
    },

    statusClass(status) {
      switch (status) {
        case 'todo':
          return 'bg-blue-100 text-blue-800 border border-blue-300';
        case 'in_progress':
          return 'bg-amber-100 text-amber-800 border border-amber-300';
        case 'review':
          return 'bg-purple-100 text-purple-800 border border-purple-300';
        case 'done':
          return 'bg-emerald-100 text-emerald-800 border border-emerald-300';
        case 'blocked':
          return 'bg-rose-100 text-rose-800 border border-rose-300';
        default:
          return 'bg-gray-100 text-gray-800 border border-gray-300';
      }
    },
    formatStatus(status) {
      return {
        todo: 'To Do',
        in_progress: 'In Progress',
        review: 'Review',
        done: 'Done',
        blocked: 'Blocked'
      }[status] || 'Unknown';
    },

    getCalendarColor(task) {
      if (task.status === "done") return "#10b981"; // green
      if (task.status === "blocked") return "#ef4444"; // red
      if (task.status === "in_progress") return "#f59e0b"; // amber
      return "#6366f1";
      },



    async openTaskFeedback(task) {
      this.selectedTask = task;
      this.showFeedbackModal = true;

      const token = localStorage.getItem("jwt_token");

      // Fetch comments
      this.taskComments = [];


      // Fetch sentiment
      const sentimentRes = await fetch(
          `http://localhost:5000/sentiment/task/${task.id}`,
          { headers: { Authorization: `Bearer ${token}` } }
      );

      if (sentimentRes.ok) {
        const data = await sentimentRes.json();
        this.overallSentiment = data.sentiment;
      }
    },

    closeFeedbackModal() {
      this.showFeedbackModal = false;
      this.selectedTask = null;
      this.taskComments = [];
      this.overallSentiment = "Neutral";
    },

    sentimentBadge(sentiment) {
      return {
        "Positive": "bg-emerald-100 text-emerald-800 border border-emerald-300",
        "Negative": "bg-rose-100 text-rose-800 border border-rose-300",
        "Neutral": "bg-gray-100 text-gray-800 border border-gray-300"
      }[sentiment] || "bg-gray-100 text-gray-800";
    },




    getAssigneeName(task) {
      // If backend already sends a name → use it
      if (task.creator_name && isNaN(task.creator_name)) {
        return task.creator_name;
      }

      // If it's a number or missing → show fallback
      return 'Unassigned';
    },

    getAssigneeRole(task) {
      return task.role || 'Member';
    },

    async loadTasks() {
      try {
        const token = localStorage.getItem("jwt_token");
        const projectId = this.$route.params.id;

        const res = await fetch(
            `http://localhost:5000/tasks/projects/${projectId}/tasks`,
            {
              headers: { Authorization: `Bearer ${token}` }
            }
        );

        if (res.ok) {
          this.tasks = await res.json();
          this.lastUpdated = new Date().toLocaleTimeString('en-US', {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true
          });
        }
      } catch (error) {
        console.error("Error loading tasks:", error);
      }
    },

    filterTasks() {
      const query = this.searchQuery.trim().toLowerCase();

      let filtered = this.tasks.filter(task => {
        const title = task.title?.toLowerCase() || '';
        const description = task.description?.toLowerCase() || '';
        const status = task.status?.toLowerCase() || '';
        const assignee = String(task.assigned_to || '').toLowerCase();

        return (
            !query ||
            title.includes(query) ||
            description.includes(query) ||
            status.includes(query) ||
            assignee.includes(query)
        );
      });

      if (this.filterStatus) {
        filtered = filtered.filter(task => task.status === this.filterStatus);
      }

      filtered.sort((a, b) => {
        let aValue = a[this.sortField] ?? '';
        let bValue = b[this.sortField] ?? '';

        if (this.sortField === 'estimated_hours') {
          aValue = Number(aValue) || 0;
          bValue = Number(bValue) || 0;
        }

        return this.sortDirection === 'asc'
            ? aValue > bValue ? 1 : -1
            : aValue < bValue ? 1 : -1;
      });

      this.filteredTasks = filtered;
    },


    sortBy(field) {
      if (this.sortField === field) {
        this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
      } else {
        this.sortField = field;
        this.sortDirection = 'asc';
      }
      this.filterTasks();
    },
    renderBurndown() {
      this.$nextTick(() => {
        if (!this.$refs.burndownChart) return;

        if (this.chart) {
          this.chart.destroy();
          this.chart = null;
        }

        const canvas = this.$refs.burndownChart;
        if (!canvas || !canvas.getContext) return;

        const ctx = canvas.getContext("2d");
        if (!ctx) return;

        const days = 7;
        const labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
        const idealData = [];
        const actualData = [];

        const totalHours = this.totalEstimatedHours || 0;
        const dailyIdealBurn = totalHours / days;

        for (let i = 0; i < days; i++) {
          idealData.push(Math.max(0, totalHours - dailyIdealBurn * i));

          const progressFactor = 0.8 + Math.random() * 0.4;
          const actualProgress = Math.min(
              totalHours,
              (totalHours * i) / days * progressFactor
          );
          actualData.push(Math.max(0, totalHours - actualProgress));
        }

        this.chart = new Chart(ctx, {
          type: "line",
          data: {
            labels,
            datasets: [
              {
                label: "Ideal Burndown",
                data: idealData,
                borderColor: '#94a3b8',
                borderDash: [5, 5],
                borderWidth: 2,
                tension: 0.4,
                pointRadius: 0
              },
              {
                label: "Actual Progress",
                data: actualData,
                borderColor: '#6366f1',
                backgroundColor: 'rgba(99, 102, 241, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointRadius: 4
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: false,
            animations: false,
          }
        });
      });
    }
  },

  watch: {
    tasks: {
      handler() {
        this.filterTasks();
        this.renderBurndown();
      },
      deep: true
    }
  }
};




</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
  font-family: 'Inter', sans-serif;
}

/* Custom animations */
@keyframes slide-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.animate-slide-up {
  animation: slide-up 0.6s ease-out forwards;
}

.animate-fade-in {
  animation: fade-in 0.8s ease-out forwards;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(to bottom, #6366f1, #8b5cf6);
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(to bottom, #4f46e5, #7c3aed);
}

/* Smooth transitions */
* {
  transition: background-color 0.3s ease,
  border-color 0.3s ease,
  transform 0.3s ease,
  opacity 0.3s ease;
}

/* Line clamp utility */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Glass effect */
.glass {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.fc {
  --fc-border-color: rgba(0,0,0,0.05);
  --fc-today-bg-color: rgba(99,102,241,0.1);
  font-family: 'Inter', sans-serif;
}

.fc-event {
  border-radius: 8px;
  font-size: 0.75rem;
  padding: 2px 6px;
}

</style>