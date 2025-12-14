<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50 p-6">
    <!-- Header -->
    <header class="bg-white rounded-2xl shadow-sm p-6 mb-8 border border-gray-100">
      <div class="flex justify-between items-center">
        <div class="flex items-center space-x-4">
          <div class="w-12 h-12 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
          </div>
          <div>
            <h1 class="text-2xl font-bold text-gray-800">Admin Dashboard</h1>
            <p class="text-gray-600">Manage your projects and team members</p>
          </div>
        </div>
        <button
            @click="handleLogout"
            class="flex items-center space-x-2 px-6 py-3 bg-gradient-to-r from-red-500 to-red-600 text-white rounded-xl hover:from-red-600 hover:to-red-700 transition-all duration-300 transform hover:-translate-y-0.5 shadow-lg"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
          </svg>
          <span>Logout</span>
        </button>
      </div>
    </header>

    <!-- Stats Overview -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Projects</p>
            <p class="text-3xl font-bold text-gray-800 mt-2">{{ projects.length }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-xl">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Active Members</p>
            <p class="text-3xl font-bold text-gray-800 mt-2">{{ totalMembers }}</p>
          </div>
          <div class="p-3 bg-green-100 rounded-xl">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Upcoming Deadlines</p>
            <p class="text-3xl font-bold text-gray-800 mt-2">{{ upcomingDeadlines }}</p>
          </div>
          <div class="p-3 bg-yellow-100 rounded-xl">
            <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Completed</p>
            <p class="text-3xl font-bold text-gray-800 mt-2">{{ completedProjects }}</p>
          </div>
          <div class="p-3 bg-purple-100 rounded-xl">
            <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Projects Section -->
    <section class="mb-8">
      <div class="flex justify-between items-center mb-6">
        <div>
          <h2 class="text-2xl font-bold text-gray-800">Project Management</h2>
          <p class="text-gray-600 mt-1">Create and manage your team projects</p>
        </div>
        <button
            @click="openProjectModal()"
            class="flex items-center space-x-2 px-6 py-3 bg-gradient-to-r from-indigo-500 to-indigo-600 text-white rounded-xl hover:from-indigo-600 hover:to-indigo-700 transition-all duration-300 transform hover:-translate-y-0.5 shadow-lg"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
          </svg>
          <span>New Project</span>
        </button>
      </div>

      <div v-if="projects.length === 0" class="bg-white rounded-2xl p-12 text-center border border-gray-200">
        <svg class="w-16 h-16 text-gray-300 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"/>
        </svg>
        <h3 class="text-xl font-semibold text-gray-700 mb-2">No projects yet</h3>
        <p class="text-gray-500 mb-6">Get started by creating your first project</p>
        <button
            @click="openProjectModal()"
            class="px-6 py-3 bg-indigo-600 text-white rounded-xl hover:bg-indigo-700 transition-colors"
        >
          Create Project
        </button>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
            v-for="project in projects"
            :key="project.id"
            class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100 hover:shadow-lg transition-all duration-300 transform hover:-translate-y-1 relative group"
        >
          <!-- Status Badge -->
          <div class="absolute top-4 right-4">
            <span :class="[
              'px-3 py-1 rounded-full text-xs font-medium',
              getDaysUntilDeadline(project.deadline) <= 7 ? 'bg-red-100 text-red-800' :
              getDaysUntilDeadline(project.deadline) <= 30 ? 'bg-yellow-100 text-yellow-800' :
              'bg-green-100 text-green-800'
            ]">
              {{ formatDeadline(project.deadline) }}
            </span>
          </div>

          <!-- Project Icon -->
          <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-4">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"/>
            </svg>
          </div>

          <h3 class="text-lg font-bold text-gray-800 mb-2">{{ project.title }}</h3>
          <p class="text-gray-600 text-sm mb-4 line-clamp-2">{{ project.description }}</p>

          <!-- Project Meta -->
          <div class="flex items-center justify-between text-sm text-gray-500 mb-4">
            <div class="flex items-center space-x-1">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span>{{ formatDate(project.deadline) }}</span>
            </div>
            <div class="flex items-center space-x-1">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
              </svg>
              <span>{{ project.members.length }} members</span>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex justify-between pt-4 border-t border-gray-100">
            <button
                @click="openProjectModal(project)"
                class="flex items-center space-x-1 text-blue-600 hover:text-blue-700 transition-colors group"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
              </svg>
              <span class="text-sm font-medium">Edit</span>
            </button>

            <button
                @click="openInviteModal(project)"
                class="flex items-center space-x-1 text-green-600 hover:text-green-700 transition-colors group"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
              </svg>
              <span class="text-sm font-medium">Invite Member</span>
            </button>

            <button
                @click="deleteProject(project.id)"
                class="flex items-center space-x-1 text-red-600 hover:text-red-700 transition-colors group"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
              </svg>
              <span class="text-sm font-medium">Delete</span>
            </button>
            <button
                @click="$router.push(`/admin/projects/${project.id}/tasks`)"
                class="text-indigo-600 hover:text-indigo-800 text-sm font-medium"
            >
              View Tasks →
            </button>

          </div>
        </div>
      </div>
    </section>

    <!-- Project Modal -->
    <div
        v-if="showProjectModal"
        class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
    >
      <div class="bg-white rounded-2xl shadow-xl w-full max-w-md">
        <div class="px-6 py-4 border-b border-gray-200">
          <h3 class="text-xl font-semibold text-gray-800">
            {{ currentProject ? "Edit Project" : "Create New Project" }}
          </h3>
        </div>

        <form @submit.prevent="saveProject" class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Project Title</label>
            <input
                v-model="projectForm.title"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
                placeholder="Enter project title"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
            <textarea
                v-model="projectForm.description"
                required
                rows="3"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
                placeholder="Describe the project..."
            ></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Deadline</label>
            <input
                v-model="projectForm.deadline"
                type="date"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
            />
          </div>

          <div class="flex justify-end space-x-3 pt-4">
            <button
                type="button"
                @click="closeProjectModal"
                class="px-6 py-3 text-gray-700 border border-gray-300 rounded-xl hover:bg-gray-50 transition-colors"
            >
              Cancel
            </button>
            <button
                type="submit"
                class="px-6 py-3 bg-indigo-600 text-white rounded-xl hover:bg-indigo-700 transition-colors"
            >
              {{ currentProject ? "Update" : "Create" }} Project
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Invitation Modal -->
    <div
        v-if="showInviteModal"
        class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
    >
      <div class="bg-white rounded-2xl shadow-xl w-full max-w-md">
        <div class="px-6 py-4 border-b border-gray-200">
          <h3 class="text-xl font-semibold text-gray-800">
            Invite Member to {{ selectedProject?.title }}
          </h3>
        </div>

        <form @submit.prevent="sendInvitation" class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Member Email</label>
            <input
                v-model="inviteForm.email"
                type="email"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
                placeholder="member@example.com"
            />
            <p class="text-sm text-gray-500 mt-1">
              An invitation email will be sent to this address
            </p>
          </div>

          <div class="flex justify-end space-x-3 pt-4">
            <button
                type="button"
                @click="closeInviteModal"
                class="px-6 py-3 text-gray-700 border border-gray-300 rounded-xl hover:bg-gray-50 transition-colors"
            >
              Cancel
            </button>
            <button
                type="submit"
                :disabled="sendingInvitation"
                class="px-6 py-3 bg-indigo-600 text-white rounded-xl hover:bg-indigo-700 transition-colors disabled:opacity-50"
            >
              {{ sendingInvitation ? 'Sending...' : 'Send Invitation' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      projects: [],
      totalMembers: 0,
      upcomingDeadlines: 0,
      completedProjects: 0,

      showProjectModal: false,
      showInviteModal: false,

      currentProject: null,
      selectedProject: null,

      projectForm: {
        title: "",
        description: "",
        deadline: "",
      },

      inviteForm: {
        email: "",
      },

      sendingInvitation: false
    };
  },

  mounted() {
    this.loadProjects();
  },

  methods: {
    // -------------------------
    // Load Projects from Backend
    // -------------------------
    async loadProjects() {
      try {
        const response = await fetch("http://localhost:5000/projects/");
        if (!response.ok) throw new Error("Failed to fetch projects");
        this.projects = await response.json();

        // Calculate stats
        this.totalMembers = this.projects.reduce((sum, project) => sum + project.members.length, 0);

        // Calculate upcoming deadlines (within 30 days)
        const today = new Date();
        this.upcomingDeadlines = this.projects.filter(project => {
          const deadline = new Date(project.deadline);
          const diffDays = Math.ceil((deadline - today) / (1000 * 60 * 60 * 24));
          return diffDays > 0 && diffDays <= 30;
        }).length;

      } catch (err) {
        console.error("Error loading projects:", err);
        alert("Failed to load projects");
      }
    },

    // -------------------------
    // Project Modal Open / Close
    // -------------------------
    openProjectModal(project = null) {
      if (project) {
        this.currentProject = project;
        this.projectForm = { ...project };
      } else {
        this.currentProject = null;
        this.projectForm = { title: "", description: "", deadline: "" };
      }
      this.showProjectModal = true;
    },

    closeProjectModal() {
      this.showProjectModal = false;
      this.currentProject = null;
    },

    async saveProject() {
      if (!this.projectForm.title || !this.projectForm.deadline) return;

      try {
        let response;
        if (this.currentProject) {
          // UPDATE
          response = await fetch(`http://localhost:5000/projects/${this.currentProject.id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.projectForm),
          });
        } else {
          // CREATE
          response = await fetch("http://localhost:5000/projects/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.projectForm),
          });
        }

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || "Failed to save project");
        }

        await this.loadProjects(); // refresh projects from backend
        this.closeProjectModal();
        alert("Project saved successfully!");
      } catch (err) {
        console.error("Error saving project:", err);
        alert("Error: " + err.message);
      }
    },

    // -------------------------
    // DELETE Project
    // -------------------------
    async deleteProject(id) {
      if (!confirm("Are you sure you want to delete this project?")) return;

      try {
        const response = await fetch(`http://localhost:5000/projects/${id}`, {
          method: "DELETE",
        });
        if (!response.ok) throw new Error("Failed to delete project");

        this.projects = this.projects.filter((p) => p.id !== id);
        alert("Project deleted successfully!");
      } catch (err) {
        console.error("Error deleting project:", err);
        alert("Failed to delete project");
      }
    },

    // -------------------------
    // INVITATION Modal
    // -------------------------
    openInviteModal(project) {
      this.selectedProject = project;
      this.inviteForm.email = "";
      this.showInviteModal = true;
    },

    closeInviteModal() {
      this.showInviteModal = false;
      this.selectedProject = null;
      this.inviteForm.email = "";
      this.sendingInvitation = false;
    },

// In AdminDashboard.vue - sendInvitation method
    // Fixed sendInvitation method for AdminDashboard.vue
    // Fixed sendInvitation method for AdminDashboard.vue
    async sendInvitation() {
      if (!this.inviteForm.email || !this.selectedProject) return;

      this.sendingInvitation = true;

      try {
        // ✅ Try both keys for compatibility
        let token = localStorage.getItem("jwt_token");
        if (!token) {
          token = localStorage.getItem("token");
        }

        // Debug logging
        console.log("🔍 Checking localStorage...");
        console.log("🔍 All keys:", Object.keys(localStorage));
        console.log("🔍 jwt_token exists?", localStorage.getItem("jwt_token") ? "YES" : "NO");
        console.log("🔍 token exists?", localStorage.getItem("token") ? "YES" : "NO");

        if (token) {
          console.log("✅ Token found!");
          console.log("🎫 Token preview:", token.substring(0, 50) + "...");
          console.log("🎫 Token length:", token.length);

          // Verify token format
          const parts = token.split('.');
          console.log("🎫 Token parts:", parts.length, "(should be 3)");

          if (parts.length !== 3) {
            console.error("❌ Invalid JWT format! Token has", parts.length, "parts");
            alert("Invalid authentication token format. Please log in again.");
            localStorage.clear();
            this.$router.push("/LoginPage");
            return;
          }
        } else {
          console.error("❌ No token found in localStorage!");
        }

        if (!token) {
          alert("No authentication token found. Please log in again.");
          this.closeInviteModal();
          localStorage.clear();
          this.$router.push("/LoginPage");
          return;
        }

        console.log("📤 Sending invitation request...");
        console.log("📧 Email:", this.inviteForm.email);
        console.log("📁 Project ID:", this.selectedProject.id);

        const requestBody = {
          email: this.inviteForm.email,
          project_id: this.selectedProject.id
        };

        console.log("📦 Request body:", requestBody);

        const response = await fetch("http://localhost:5000/invitation/send-invitation", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
          },
          body: JSON.stringify(requestBody)
        });

        console.log("📥 Response status:", response.status);

        const data = await response.json();
        console.log("📥 Response data:", data);

        if (!response.ok) {
          // Special handling for JWT errors
          if (data.msg && data.msg.includes("Not enough segments")) {
            console.error("❌ JWT Format Error - Token is invalid");
            alert("Authentication token is invalid. Please log in again.");
            localStorage.clear();
            this.$router.push("/LoginPage");
            return;
          }

          throw new Error(data.message || data.msg || `HTTP ${response.status}: ${response.statusText}`);
        }

        alert(`✅ Invitation sent successfully to ${this.inviteForm.email}!`);
        this.closeInviteModal();
      } catch (error) {
        console.error("❌ Error sending invitation:", error);

        if (error.message.includes("401") ||
            error.message.includes("Unauthorized") ||
            error.message.includes("Not enough segments") ||
            error.message.includes("token")) {
          alert("Your session has expired or is invalid. Please log in again.");
          localStorage.clear();
          this.$router.push("/LoginPage");
        } else if (error.message.includes("403")) {
          alert("Only admins can send invitations. Please log in as an admin user.");
        } else {
          alert("Error: " + error.message);
        }
      } finally {
        this.sendingInvitation = false;
      }
    },

    // -------------------------
    // HELPERS
    // -------------------------
    getDaysUntilDeadline(deadline) {
      const today = new Date();
      const due = new Date(deadline);
      const diff = (due - today) / (1000 * 60 * 60 * 24);
      return Math.ceil(diff);
    },

    formatDeadline(d) {
      const days = this.getDaysUntilDeadline(d);
      if (days < 0) return "Overdue";
      if (days === 0) return "Due today";
      if (days === 1) return "1 day left";
      return `${days} days left`;
    },

    formatDate(dateString) {
      if (!dateString) return "No date";
      try {
        return new Date(dateString).toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric'
        });
      } catch (e) {
        return dateString;
      }
    },

    // -------------------------
    // LOGOUT
    // -------------------------
    handleLogout() {
      localStorage.clear();
      this.$router.push("/LoginPage");
    },
  },
};
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Add smooth transitions for modals */
.fixed {
  transition: opacity 0.3s ease;
}

/* Style for the invitation modal */
.bg-opacity-50 {
  backdrop-filter: blur(4px);
}

/* Improve button hover effects */
button:disabled {
  cursor: not-allowed;
}

/* Style for the project cards */
.group:hover .group-hover\:shadow-lg {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

/* Status badge styles */
.bg-red-100 { background-color: #fee2e2; }
.text-red-800 { color: #991b1b; }
.bg-yellow-100 { background-color: #fef3c7; }
.text-yellow-800 { color: #92400e; }
.bg-green-100 { background-color: #d1fae5; }
.text-green-800 { color: #065f46; }
</style>