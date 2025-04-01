<script setup>
import { ref, onMounted } from 'vue'

onMounted(() => {
  console.log("hello world")
  window.location.href="/introduction";
})
</script>
