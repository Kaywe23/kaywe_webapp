<template>
  <header class="sticky top-0 z-20 border-b border-white/10 bg-slate-950/45 backdrop-blur-xl">
    <nav class="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-3">
        <img :src="logoUrl" alt="KAYWE Logo" class="h-10 w-auto rounded-md border border-white/10 object-contain" />
        <div>
          <p class="text-xs uppercase tracking-[0.35em] text-blue-300/80">DJ / Producer</p>
          <p class="text-lg font-semibold tracking-wide">KAYWE</p>
        </div>
      </div>
      <ul class="hidden gap-6 text-sm text-slate-200 md:flex">
        <li><a href="#about" class="transition hover:text-white">About</a></li>
        <li><a href="#sound" class="transition hover:text-white">Sound</a></li>
        <li><a href="#live" class="transition hover:text-white">Live</a></li>
        <li><a href="#booking" class="transition hover:text-white">Booking</a></li>
      </ul>
    </nav>
  </header>
</template>

<script setup>
import logoUrl from '../assets/kaywe-logo.svg'
</script>
