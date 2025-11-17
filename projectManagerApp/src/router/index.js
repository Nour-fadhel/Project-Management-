// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/HomePage.vue';
import LoginPage from '../components/LoginPage.vue';
import SignupPage from '../components/SignupPage.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/LoginPage',
        name: 'LoginPage',
        component: LoginPage,
    },
    {
        path: '/SignupPage',
        name: 'SignupPage',
        component: SignupPage,
    }
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL), // Use HTML5 History API
    routes,
});

export default router;