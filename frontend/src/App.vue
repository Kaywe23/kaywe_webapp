<template>
  <div class="min-h-screen text-slate-100">
    <Navbar />

    <main>
      <HeroSection />

      <section id="about" class="px-4 pb-12 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-6xl">
          <article class="liquid-glass rounded-3xl p-6 sm:p-8 lg:p-10">
            <p class="text-xs uppercase tracking-[0.3em] text-blue-200/80">About</p>
            <h2 class="mt-3 text-3xl font-semibold sm:text-4xl">KAYWE ist elektronische Präzision mit maximaler Energie.</h2>
            <div class="mt-6 space-y-4 text-sm leading-relaxed text-slate-200 sm:text-base">
              <p>
                KAYWE ist ein DJ mit Fokus auf modernen House- und Techno-Sound – kombiniert mit vielseitigen
                Mixed-Music-Elementen für maximale Flexibilität.
              </p>
              <p>
                Sein Stil ist klar, energiegeladen und dynamisch. Kein zufälliges Aneinanderreihen von Tracks – jedes
                Set ist eine bewusst aufgebaute Reise.
              </p>
              <p>
                Von deepen House-Vibes bis zu kraftvollem Peak-Time-Techno schafft er Spannungsbögen, die den
                Dancefloor kontrolliert eskalieren lassen.
              </p>
            </div>
          </article>
        </div>
      </section>

      <section id="sound" class="px-4 pb-12 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-6xl">
          <h3 class="text-2xl font-semibold sm:text-3xl">Sound</h3>
          <p class="mt-3 max-w-3xl text-sm text-slate-300 sm:text-base">
            KAYWE versteht es, Genregrenzen zu verbinden und die Energie im Raum präzise zu lesen.
          </p>
          <div class="mt-6 grid gap-4 md:grid-cols-3">
            <SetListCard title="House" subtitle="Groovy, rhythmisch, treibend." />
            <SetListCard title="Techno" subtitle="Hypnotisch, druckvoll, intensiv." />
            <SetListCard title="Mixed Music" subtitle="Flexibel, crowd-orientiert, überraschend." />
          </div>
        </div>
      </section>

      <section id="live" class="px-4 pb-12 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-6xl">
          <article class="liquid-glass rounded-3xl p-6 sm:p-8">
            <p class="text-xs uppercase tracking-[0.3em] text-violet-200/80">Live Experience</p>
            <h3 class="mt-3 text-2xl font-semibold sm:text-3xl">Was ein KAYWE-Set ausmacht</h3>
            <ul class="mt-6 grid gap-3 sm:grid-cols-2">
              <li v-for="item in livePoints" :key="item" class="rounded-2xl border border-white/15 bg-white/5 px-4 py-3 text-sm text-slate-200">
                {{ item }}
              </li>
            </ul>
            <p class="mt-6 text-sm text-slate-300 sm:text-base">Es geht nicht nur um Musik – es geht um Atmosphäre.</p>
          </article>
        </div>
      </section>

      <BookingCard />
    </main>
  </div>
</template>

<script setup>
import BookingCard from './components/BookingCard.vue'
import HeroSection from './components/HeroSection.vue'
import Navbar from './components/Navbar.vue'
import SetListCard from './components/SetListCard.vue'

const livePoints = [
  'Dynamischer Spannungsaufbau',
  'Saubere, präzise Übergänge',
  'Tiefer Fokus auf Groove & Drive',
  'Energie, die den Raum trägt',
]
</script>
