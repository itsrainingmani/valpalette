<script>
import { onMount } from "svelte";
import colorsData from "./data/colors.json";
import weaponNames from "./data/skin_names.json";
import { selectedGun } from "./stores";

let colors = [];
let pixelated = false;

function onKeyPress(e) {
	if (e.key === "p") {
		pixelated = !pixelated;
	}
}

function calcFontColor(hex_color) {
	let rgb = hex_color.match(/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i);
	rgb.shift();
	rgb = rgb.map((x) => Number.parseInt(x, 16));
	const sum = Math.round(
		(Number.parseInt(rgb[0]) * 299 +
			Number.parseInt(rgb[1]) * 587 +
			Number.parseInt(rgb[2]) * 114) /
			1000,
	);
	return sum > 128 ? "black" : "white";
}

function copyToClipboard(text) {
	navigator.clipboard.writeText(text).then(
		() => {
			console.log("Color copied to clipboard!");
		},
		(err) => {
			console.error("Could not copy text: ", err);
		},
	);
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
			{#each colors as color, i}
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<!-- svelte-ignore a11y-no-static-element-interactions -->
				<div
					class="row"
					style="background-color: {colors[i] || '#ffffff'}"
					title={color}
					on:click={() => copyToClipboard(color)}
				>
					<span class="color-hex" style={`color: ${calcFontColor(color)}`}
						>{color.toUpperCase()}{" "}<span class="copy-msg" style={`color: ${calcFontColor(color)}`}>copied to clipboard</span></span
					>
				</div>
			{/each}
		</div>
		<div class="image-container">
			<img
				id="gun-image"
				src={`${import.meta.env.BASE_URL}/${pixelated ? "pixelated" : "skins"}/${colorsData[$selectedGun]?.type}/${$selectedGun}.png`}
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

	.row {
		position: relative;
		height: auto;
	}

	.row:hover {
		cursor: pointer;
	}

	.color-hex {
		user-select: none;
		position: absolute;
		top: 50%;
		left: 10px;
		transform: translateY(-50%);
		font-size: 15px;
		font-family: "The Future", monospace;
		font-weight: bold;
	}

	.copy-msg {
    font-size: 11px;
    font-style: italic;
    opacity: 0;
    transition: opacity 0.1s ease-in-out;
  }

  .row:active .copy-msg {
    opacity: 1;
    animation: fadeOut 2s forwards;
    animation-delay: 0.2s;
  }

  @keyframes fadeOut {
    from { opacity: 1; }
    to { opacity: 0; }
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
    content: '\25BC';
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
