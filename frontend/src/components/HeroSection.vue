<template>
  <section class="relative overflow-hidden px-4 pb-16 pt-16 sm:px-6 lg:px-8 lg:pt-24">
    <div class="mx-auto grid max-w-6xl gap-10 lg:grid-cols-[1.15fr_0.85fr] lg:items-center">
      <div class="space-y-6">
        <img :src="logoUrl" alt="KAYWE Logo" class="h-20 w-auto rounded-lg border border-white/10 object-contain p-2" />
        <p class="inline-flex items-center rounded-full border border-blue-300/30 bg-blue-400/10 px-4 py-1 text-xs uppercase tracking-[0.28em] text-blue-200">
          House • Techno • Pure Energy
        </p>
        <h1 class="text-5xl font-semibold leading-tight sm:text-6xl lg:text-7xl">
          KAYWE
        </h1>
        <p class="text-lg text-slate-200 sm:text-xl">Sound ohne Kompromisse.</p>
        <p class="max-w-2xl text-base text-slate-300 sm:text-lg">
          Druckvolle Grooves, hypnotische Builds und treibende Drops – KAYWE steht für elektronische Musik mit
          Intensität.
        </p>
        <p class="max-w-2xl text-base text-slate-300 sm:text-lg">
          Ob Underground-Club oder Mainfloor – wenn KAYWE übernimmt, verschmelzen Rhythmus und Crowd zu einer Einheit.
        </p>
        <div class="flex flex-wrap gap-3">
          <a href="#booking" class="rounded-full bg-gradient-to-r from-blue-500 to-violet-500 px-6 py-3 text-sm font-medium text-white transition hover:scale-[1.02]">Booking anfragen</a>
          <a href="#sound" class="rounded-full border border-white/20 px-6 py-3 text-sm font-medium text-white/90 transition hover:border-white/40 hover:text-white">Sound entdecken</a>
        </div>
      </div>

      <div class="relative">
        <div class="glow-ring"></div>
        <article class="liquid-glass relative rounded-3xl p-6 sm:p-8">
          <p class="text-xs uppercase tracking-[0.3em] text-violet-200/80">Signature Vibe</p>
          <h3 class="mt-3 text-2xl font-semibold">Club Pressure. Emotional Control.</h3>
          <div class="mt-6 space-y-4 text-sm text-slate-200">
            <div class="flex items-center justify-between rounded-2xl border border-white/15 bg-white/5 px-4 py-3">
              <span>Groove</span>
              <span class="text-violet-200">Druckvoll</span>
            </div>
            <div class="flex items-center justify-between rounded-2xl border border-white/15 bg-white/5 px-4 py-3">
              <span>Build</span>
              <span class="text-blue-200">Hypnotisch</span>
            </div>
            <div class="flex items-center justify-between rounded-2xl border border-white/15 bg-white/5 px-4 py-3">
              <span>Drop</span>
              <span class="text-fuchsia-200">Treibend</span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
import logoUrl from '../assets/kaywe-logo.svg'
</script>
