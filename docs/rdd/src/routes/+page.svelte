<script module>
  export const frontmatter  = {
		home: false
  }
</script>

<script>
	import { onMount } from 'svelte';

	onMount(() => {
			window.location.href = '/introduction';
	});
</script>
