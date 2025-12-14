import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../components/LoginPage.vue'
import SignupPage from '../components/SignupPage.vue';
import AdminDashboard from '../components/AdminDashboard.vue';
import MemberDashboard from '../components/MemberDashboard.vue';
import HomePage from '../components/HomePage.vue';
import RegisterWithInvitation from '../components/RegisterWithInvitation.vue';
import AdminProjectTasks from "@/components/AdminProjectTasks.vue";
const routes = [
    { path: "/LoginPage", component: LoginPage },
    { path: "/SignupPage", component: SignupPage },
    { path: "/", component: HomePage},

    {
        path: "/AdminDashboard",
        component: AdminDashboard,
        meta: { requiresAuth: true, role: "admin" }
    },
    {
        path: "/MemberDashboard",
        component: MemberDashboard,
        meta: { requiresAuth: true, role: "member" }
    },
    {
        path: '/register',
        name: 'RegisterWithInvitation',
        component: RegisterWithInvitation
    },
    {
        path: "/admin/projects/:id/tasks",
        name: "AdminProjectTasks",
        component: AdminProjectTasks
    }

];
const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem("token");
    const role = localStorage.getItem("role");

    console.log("Navigation guard - To:", to.path, "Role:", role); // Debug

    if (to.meta.requiresAuth) {
        if (!token) {
            console.log("No token, redirecting to login"); // Debug
            next("/LoginPage");
        } else if (to.meta.role && to.meta.role !== role) {
            console.log("Wrong role. Expected:", to.meta.role, "Got:", role); // Debug
            // Redirect to correct dashboard based on role
            if (role === "admin") {
                next("/AdminDashboard");
            } else {
                next("/MemberDashboard");
            }
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router;
