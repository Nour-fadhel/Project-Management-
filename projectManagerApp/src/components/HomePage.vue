<template>
  <div class="font-sans text-gray-900 bg-gray-50 min-h-screen">

    <!-- Header amélioré -->
    <header class="bg-white shadow-lg sticky top-0 z-50 transition-all duration-300">
      <div class="container mx-auto flex justify-between items-center px-4 sm:px-6 py-4">
        <div class="flex items-center space-x-2">
          <div class="w-8 h-8 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-lg flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z" clip-rule="evenodd" />
            </svg>
          </div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">ProjectManager</h1>
        </div>

        <!-- Navigation pour desktop -->
        <nav class="hidden md:flex space-x-6 text-gray-700 font-medium">
          <a href="#" class="hover:text-indigo-600 transition-all duration-300 relative after:absolute after:bottom-0 after:left-0 after:w-0 after:h-0.5 after:bg-indigo-600 after:transition-all after:duration-300 hover:after:w-full">Accueil</a>
          <a href="#features" class="hover:text-indigo-600 transition-all duration-300 relative after:absolute after:bottom-0 after:left-0 after:w-0 after:h-0.5 after:bg-indigo-600 after:transition-all after:duration-300 hover:after:w-full">Fonctionnalités</a>
          <a href="#pricing" class="hover:text-indigo-600 transition-all duration-300 relative after:absolute after:bottom-0 after:left-0 after:w-0 after:h-0.5 after:bg-indigo-600 after:transition-all after:duration-300 hover:after:w-full">Tarifs</a>
          <router-link to="/LoginPage">
            <button class="bg-gradient-to-r from-indigo-500 to-indigo-600 text-white px-4 py-2 rounded-lg hover:from-indigo-600 hover:to-indigo-700 transition-all duration-300 shadow-md">
              Connexion
            </button>
          </router-link>        </nav>

        <!-- Menu mobile -->
        <button class="md:hidden text-gray-700 focus:outline-none" @click="mobileMenuOpen = !mobileMenuOpen">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>

      <!-- Menu mobile déroulant -->
      <div v-if="mobileMenuOpen" class="md:hidden bg-white py-4 px-6 shadow-lg">
        <div class="flex flex-col space-y-4">
          <a href="#" class="text-gray-700 hover:text-indigo-600 transition">Accueil</a>
          <a href="#features" class="text-gray-700 hover:text-indigo-600 transition" @click="mobileMenuOpen = false">Fonctionnalités</a>
          <a href="#pricing" class="text-gray-700 hover:text-indigo-600 transition" @click="mobileMenuOpen = false">Tarifs</a>
          <a href="#" class="bg-gradient-to-r from-indigo-500 to-indigo-600 text-white px-4 py-2 rounded-lg text-center hover:from-indigo-600 hover:to-indigo-700 transition">Connexion</a>
        </div>
      </div>
    </header>

    <!-- Hero amélioré -->
    <section class="relative bg-gradient-to-br from-white via-indigo-50 to-purple-50 py-24 md:py-32 overflow-hidden">
      <!-- Éléments décoratifs -->
      <div class="absolute top-10 left-10 w-20 h-20 bg-indigo-200 rounded-full opacity-50 blur-xl"></div>
      <div class="absolute bottom-10 right-10 w-32 h-32 bg-purple-200 rounded-full opacity-50 blur-xl"></div>

      <div class="container mx-auto flex flex-col-reverse md:flex-row items-center px-6 relative z-10">
        <div class="md:w-1/2 text-center md:text-left mt-10 md:mt-0">
          <h2 class="text-4xl md:text-5xl lg:text-6xl font-extrabold mb-6 leading-tight">
            Gérez vos projets <span class="bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">efficacement</span>
          </h2>
          <p class="text-lg md:text-xl text-gray-600 mb-8 max-w-lg mx-auto md:mx-0">
            Créez vos projets, organisez vos tâches, collaborez en temps réel et boostez votre productivité.
          </p>
          <div class="flex justify-center md:justify-start gap-4 flex-wrap">
            <button class="bg-gradient-to-r from-indigo-500 to-indigo-600 text-white font-semibold px-8 py-4 rounded-lg shadow-lg hover:from-indigo-600 hover:to-indigo-700 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-xl flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z" clip-rule="evenodd" />
              </svg>
              Commencer Gratuitement
            </button>
            <button class="border border-indigo-600 text-indigo-600 px-8 py-4 rounded-lg hover:bg-indigo-50 transition-all duration-300 transform hover:-translate-y-1 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
              </svg>
              Demander une démo
            </button>
          </div>
          <p class="mt-6 text-gray-500 text-sm">Aucune carte de crédit requise • Essai gratuit de 14 jours</p>
        </div>
        <div class="md:w-1/2 mb-10 md:mb-0 flex justify-center">
          <div class="relative max-w-md">
            <div class=" rounded-lg  "></div>
            <img src="@/assets/Suivi-projet-removebg-preview.png" alt="Illustration Hero" class="relative rounded-lg  transform hover:scale-105 transition duration-500">
          </div>
        </div>
      </div>
    </section>

    <!-- Fonctionnalités MVP améliorées -->
    <section id="features" class="relative py-24 bg-gradient-to-b from-white to-indigo-50">
      <div class="container mx-auto px-6">
        <div class="text-center mb-16">
          <span class="text-indigo-600 font-semibold text-sm uppercase tracking-wider">Fonctionnalités</span>
          <h3 class="text-3xl md:text-4xl font-bold text-gray-800 mt-2">Tout ce dont vous avez besoin</h3>
          <p class="text-gray-600 max-w-2xl mx-auto mt-4">Découvrez les fonctionnalités qui feront de ProjectManager votre outil de gestion de projets préféré.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Carte exemple améliorée -->
          <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300 border border-gray-100">
            <div class="text-indigo-600 mb-4 bg-indigo-50 w-16 h-16 rounded-lg flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <h4 class="text-xl font-semibold mb-2 text-gray-800 text-center">Authentification sécurisée</h4>
            <p class="text-gray-600 text-center">Inscription, connexion et profil utilisateur avec protection des données.</p>
          </div>

          <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300 border border-gray-100">
            <div class="text-indigo-600 mb-4 bg-indigo-50 w-16 h-16 rounded-lg flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
              </svg>
            </div>
            <h4 class="text-xl font-semibold mb-2 text-gray-800 text-center">Gestion des Projets</h4>
            <p class="text-gray-600 text-center">Créez, modifiez et organisez vos projets en toute simplicité.</p>
          </div>

          <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300 border border-gray-100">
            <div class="text-indigo-600 mb-4 bg-indigo-50 w-16 h-16 rounded-lg flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2" />
              </svg>
            </div>
            <h4 class="text-xl font-semibold mb-2 text-gray-800 text-center">Tableaux Kanban</h4>
            <p class="text-gray-600 text-center">Colonnes personnalisables pour visualiser l'avancement de vos projets.</p>
          </div>

          <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300 border border-gray-100">
            <div class="text-indigo-600 mb-4 bg-indigo-50 w-16 h-16 rounded-lg flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h4 class="text-xl font-semibold mb-2 text-gray-800 text-center">Gestion des Tâches</h4>
            <p class="text-gray-600 text-center">Créez, assignez, commentez et suivez l'avancement de vos tâches.</p>
          </div>

          <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300 border border-gray-100">
            <div class="text-indigo-600 mb-4 bg-indigo-50 w-16 h-16 rounded-lg flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" />
              </svg>
            </div>
            <h4 class="text-xl font-semibold mb-2 text-gray-800 text-center">Collaboration d'équipe</h4>
            <p class="text-gray-600 text-center">Invitez des membres et gérez les rôles au sein de vos projets.</p>
          </div>

          <div class="bg-white p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300 border border-gray-100">
            <div class="text-indigo-600 mb-4 bg-indigo-50 w-16 h-16 rounded-lg flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
              </svg>
            </div>
            <h4 class="text-xl font-semibold mb-2 text-gray-800 text-center">Notifications en temps réel</h4>
            <p class="text-gray-600 text-center">Restez informé des mises à jour importantes de vos projets.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats / Pourquoi nous amélioré -->
    <section class="py-24 bg-gradient-to-br from-indigo-50 to-white relative overflow-hidden">
      <!-- Éléments décoratifs -->
      <div class="absolute top-0 right-0 w-64 h-64 bg-indigo-100 rounded-full -translate-y-32 translate-x-32 opacity-70"></div>
      <div class="absolute bottom-0 left-0 w-48 h-48 bg-purple-100 rounded-full translate-y-24 -translate-x-24 opacity-70"></div>

      <div class="container mx-auto px-6 text-center relative z-10">
        <div class="max-w-3xl mx-auto">
          <span class="text-indigo-600 font-semibold text-sm uppercase tracking-wider">Confiance</span>
          <h4 class="text-3xl md:text-4xl font-bold mb-4">Pourquoi choisir ProjectManager ?</h4>
          <p class="text-gray-600 mb-12 max-w-2xl mx-auto">Rejoignez des milliers d'équipes qui font confiance à ProjectManager pour gérer leurs projets efficacement.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-8 md:gap-12 max-w-4xl mx-auto">
          <div class="bg-white p-8 rounded-xl shadow-md border border-gray-100 transform hover:-translate-y-2 transition duration-300">
            <div class="text-5xl font-extrabold text-indigo-600 mb-2">1 000+</div>
            <div class="text-gray-700 font-medium">Projets gérés</div>
            <p class="text-gray-500 text-sm mt-2">avec succès chaque mois</p>
          </div>
          <div class="bg-white p-8 rounded-xl shadow-md border border-gray-100 transform hover:-translate-y-2 transition duration-300">
            <div class="text-5xl font-extrabold text-indigo-600 mb-2">500+</div>
            <div class="text-gray-700 font-medium">Utilisateurs actifs</div>
            <p class="text-gray-500 text-sm mt-2">dans plus de 20 pays</p>
          </div>
          <div class="bg-white p-8 rounded-xl shadow-md border border-gray-100 transform hover:-translate-y-2 transition duration-300">
            <div class="text-5xl font-extrabold text-indigo-600 mb-2">99 %</div>
            <div class="text-gray-700 font-medium">Taux de satisfaction</div>
            <p class="text-gray-500 text-sm mt-2">client selon nos utilisateurs</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA amélioré -->
    <section class="py-20 bg-gradient-to-r from-indigo-500 to-purple-600 text-white text-center relative overflow-hidden">
      <!-- Éléments décoratifs -->
      <div class="absolute top-0 left-0 w-full h-full opacity-10">
        <div class="absolute top-10 left-10 w-40 h-40 bg-white rounded-full"></div>
        <div class="absolute bottom-10 right-10 w-60 h-60 bg-white rounded-full"></div>
      </div>

      <div class="container mx-auto px-6 relative z-10">
        <h5 class="text-3xl md:text-4xl font-bold mb-6">Prêt à booster votre productivité ?</h5>
        <p class="text-indigo-100 max-w-2xl mx-auto mb-8 text-lg">Rejoignez des milliers d'équipes qui utilisent déjà ProjectManager pour gérer leurs projets plus efficacement.</p>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <button class="bg-white text-indigo-600 font-semibold px-8 py-4 rounded-lg shadow-lg hover:bg-gray-100 transition-all duration-300 transform hover:-translate-y-1 flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z" clip-rule="evenodd" />
            </svg>
            Créer un compte gratuit
          </button>
          <button class="bg-transparent border-2 border-white text-white font-semibold px-8 py-4 rounded-lg hover:bg-white hover:bg-opacity-10 transition-all duration-300 transform hover:-translate-y-1 flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
              <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" />
            </svg>
            Nous contacter
          </button>
        </div>
        <p class="mt-6 text-indigo-200 text-sm">Essai gratuit de 14 jours • Aucun engagement • Annulation à tout moment</p>
      </div>
    </section>

    <!-- Footer amélioré -->
    <footer class="bg-gray-800 text-white pt-16 pb-8">
      <div class="container mx-auto px-6">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
          <div>
            <div class="flex items-center space-x-2 mb-4">
              <div class="w-8 h-8 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-lg flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z" clip-rule="evenodd" />
                </svg>
              </div>
              <h6 class="font-bold text-xl">ProjectManager</h6>
            </div>
            <p class="text-gray-400 mb-4">La plateforme collaborative pour gérer vos projets facilement et efficacement.</p>
            <div class="flex space-x-4">
              <a href="#" class="text-gray-400 hover:text-white transition">
                <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
              </a>
              <a href="#" class="text-gray-400 hover:text-white transition">
                <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              </a>
              <a href="#" class="text-gray-400 hover:text-white transition">
                <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
              </a>
            </div>
          </div>

          <div>
            <h6 class="font-semibold text-gray-300 mb-4 uppercase tracking-wider">Produit</h6>
            <ul class="space-y-3">
              <li><a href="#" class="text-gray-400 hover:text-white transition">Fonctionnalités</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Tarifs</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Cas d'utilisation</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Intégrations</a></li>
            </ul>
          </div>

          <div>
            <h6 class="font-semibold text-gray-300 mb-4 uppercase tracking-wider">Ressources</h6>
            <ul class="space-y-3">
              <li><a href="#" class="text-gray-400 hover:text-white transition">Blog</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Documentation</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Support</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">API</a></li>
            </ul>
          </div>

          <div>
            <h6 class="font-semibold text-gray-300 mb-4 uppercase tracking-wider">Entreprise</h6>
            <ul class="space-y-3">
              <li><a href="#" class="text-gray-400 hover:text-white transition">À propos</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Carrières</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Contact</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Mentions légales</a></li>
            </ul>
          </div>
        </div>

        <div class="pt-8 mt-8 border-t border-gray-700 text-sm text-gray-400 text-center">
          <p>&copy; 2023 ProjectManager. Tous droits réservés.</p>
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup>
import { ref } from 'vue'

// État pour le menu mobile
const mobileMenuOpen = ref(false)
</script>