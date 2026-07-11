# tools/web_agents/vue_generator.py
import os

def generate_vue_sfc(component_name: str) -> str:
    """Generates a Vue 3 Single File Component using the Composition API."""
    target_dir = "./generated_assets/web_builds/vue_components"
    os.makedirs(target_dir, exist_ok=True)

    vue_code = f"""<template>
  <div class="ctrl-vue-wrapper">
    <h1>{{{{ title }}}}</h1>
    <p>Matrix connection established.</p>
  </div>
</template>

<script setup>
import {{ ref, onMounted }} from 'vue'

// ctrl Matrix: Auto-generated Vue Composition Logic
const title = ref('{component_name} Component')

onMounted(() => {{
  console.log('{component_name} has mounted.')
}})
</script>

<style scoped>
.ctrl-vue-wrapper {{
  padding: 20px;
  background: rgba(0, 255, 136, 0.05);
  border: 1px solid rgba(0, 255, 136, 0.3);
  border-radius: 8px;
  color: #00ff88;
}}
</style>
"""
    file_path = os.path.join(target_dir, f"{component_name}.vue")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(vue_code)

    return f"🟢 **Vue 3 SFC Generated:** Component mapped to `{file_path}`"
