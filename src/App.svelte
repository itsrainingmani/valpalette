<script>
	import { onMount } from "svelte";
	import colorsData from "./data/colors.json";
	import weaponNames from "./data/skin_names.json";
	import { selectedGun, showPercent } from "./stores";
	import ColorRow from "./ColorRow.svelte";

	let colors = [];

	function onKeyPress(e) {
		if (e.key === "p") {
			showPercent.set(!$showPercent);
		}
	}

	onMount(() => {
		if (location.hash.length > 1) {
			const stateParams = location.hash.slice(1).split("|");
			$selectedGun = stateParams[0];
		} else {
			const keys = Object.keys(colorsData);
			$selectedGun = keys[(keys.length * Math.random()) << 0];
			location.hash = $selectedGun;
		}
		if ($selectedGun) {
			colors = colorsData[$selectedGun]?.colors || [];
		}
	});

	$: if (selectedGun) {
		colors = colorsData[$selectedGun]?.colors || [];
	}
</script>

<main>
	<div id="horizontal-bars">
		<div class="container" id="palette-cols">
			{#each Object.entries(colors) as [color, proportion]}
				<ColorRow {color} color_width={$showPercent ? proportion : 100} />
			{/each}
		</div>
		<div class="image-container">
			<img
				id="gun-image"
				src={`${import.meta.env.BASE_URL}/skins/${colorsData[$selectedGun]?.type}/${$selectedGun}.png`}
				alt={$selectedGun}
				width="100%"
			/>
		</div>
	</div>
	<div class="dropdown">
		<select
			id="guns"
			name="weapon_name"
			bind:value={$selectedGun}
			on:change={() => {
				location.hash = $selectedGun;
			}}
		>
			<option value="">Select a gun</option>
			{#each Object.entries(weaponNames) as [smol_name, canonical_name]}
				<option value={smol_name}>{canonical_name}</option>
			{/each}
		</select>
	</div>
</main>

<svelte:window on:keypress|preventDefault={onKeyPress} />

<style>
	.container {
		display: flex;
		flex-direction: column-reverse;
		height: 100vh;
	}

	.image-container {
		position: fixed;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}

	.dropdown {
		position: absolute;
		top: 20px;
		right: 20px;
		max-width: 300px;
	}

	.dropdown select {
		width: 100%;
		padding: 10px;
		font-size: 16px;
		border: 5px solid #333;
		background-color: #fff;
		cursor: pointer;
		font-family: "Valorant";
		appearance: none;
		-moz-appearance: none;
		-webkit-appearance: none;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.dropdown::after {
		content: "\25BC";
		position: absolute;
		top: 50%;
		right: 10px;
		transform: translateY(-50%);
		pointer-events: none;
	}

	.dropdown select:focus {
		outline: none;
		border-color: #4caf50;
	}
</style>
