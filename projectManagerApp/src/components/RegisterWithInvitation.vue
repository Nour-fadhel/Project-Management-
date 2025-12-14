<template>
  <div class="min-h-screen bg-gradient-to-br from-indigo-50 to-purple-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full space-y-8">
      <!-- Header -->
      <div class="text-center">
        <div class="flex justify-center items-center space-x-2 mb-6">
          <div class="w-10 h-10 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-lg flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z" clip-rule="evenodd" />
            </svg>
          </div>
          <h1 class="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">ProjectManager</h1>
        </div>
        <h2 class="text-2xl font-bold text-gray-900">Complete Your Registration</h2>
        <p v-if="invitationDetails" class="mt-2 text-gray-600">
          You've been invited to join: <strong>{{ invitationDetails.project_name }}</strong>
        </p>
      </div>

      <!-- Registration Form -->
      <div class="mt-8 bg-white p-8 rounded-2xl shadow-lg border border-gray-100">
        <div v-if="loading" class="text-center py-8">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto"></div>
          <p class="mt-4 text-gray-600">Loading invitation details...</p>
        </div>

        <form v-else @submit.prevent="handleRegistration" class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Your Name</label>
            <input
                v-model="registrationForm.name"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
                placeholder="Enter your full name"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Email Address</label>
            <input
                v-model="registrationForm.email"
                type="email"
                required
                disabled
                class="w-full px-4 py-3 border border-gray-300 rounded-lg bg-gray-50"
                :placeholder="invitationDetails?.email || 'Email from invitation'"
            />
            <p class="text-sm text-gray-500 mt-1">This email was used for your invitation</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Create Password</label>
            <div class="relative">
              <input
                  v-model="registrationForm.password"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
                  placeholder="Create a secure password"
              />
              <button
                  type="button"
                  @click="showPassword = !showPassword"
                  class="absolute inset-y-0 right-0 pr-3 flex items-center"
              >
                <svg v-if="showPassword" class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 20 20">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L6.59 6.59m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>
                </svg>
                <svg v-else class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 20 20">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                </svg>
              </button>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Confirm Password</label>
            <input
                v-model="registrationForm.confirmPassword"
                type="password"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
                placeholder="Confirm your password"
            />
          </div>

          <button
              type="submit"
              :disabled="registering"
              class="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-gradient-to-r from-indigo-500 to-indigo-600 hover:from-indigo-600 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-300 transform hover:-translate-y-0.5 disabled:opacity-50"
          >
            {{ registering ? 'Creating Account...' : 'Create Account & Join Project' }}
          </button>
        </form>

        <div v-if="error" class="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
          <p class="text-red-700">{{ error }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const loading = ref(true);
const registering = ref(false);
const showPassword = ref(false);
const error = ref("");
const invitationDetails = ref(null);

const registrationForm = ref({
  name: "",
  email: "",
  password: "",
  confirmPassword: ""
});

onMounted(async () => {
  const token = route.query.token;

  if (!token) {
    error.value = "Invalid invitation link. No token provided.";
    loading.value = false;
    return;
  }

  try {
    const response = await fetch(`http://localhost:5000/invitation/validate-invitation/${token}`);
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || "Invalid invitation");
    }

    invitationDetails.value = data;
    registrationForm.value.email = data.email;
  } catch (err) {
    error.value = err.message || "Failed to validate invitation";
  } finally {
    loading.value = false;
  }
});

const handleRegistration = async () => {
  // Validate passwords match
  if (registrationForm.value.password !== registrationForm.value.confirmPassword) {
    error.value = "Passwords do not match";
    return;
  }

  // Validate password length
  if (registrationForm.value.password.length < 6) {
    error.value = "Password must be at least 6 characters";
    return;
  }

  registering.value = true;
  error.value = "";

  try {
    const response = await fetch("http://localhost:5000/invitation/register-with-invitation", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        token: route.query.token,
        name: registrationForm.value.name,
        password: registrationForm.value.password
      })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || "Registration failed");
    }

    // Registration successful - redirect to login
    alert("Account created successfully! You can now log in.");
    router.push("/LoginPage");

  } catch (err) {
    error.value = err.message || "Registration failed";
  } finally {
    registering.value = false;
  }
};
</script>