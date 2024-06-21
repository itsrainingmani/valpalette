<script>
	import { onMount } from 'svelte';
	import colorsData from './data/colors.json';

	let keys = Object.keys(colorsData);
	console.log(keys);
	let selectedGun = keys[(keys.length * Math.random()) << 0];
	let colors = [];

	let pixelated = false;

	function onKeyPress(e) {
		if (e.key === 'p') {
			pixelated = !pixelated;
		}
	}

	/**
	 * @param {string} hex_color
	 */
	function calcFontColor(hex_color) {
		var rgb = hex_color.match(/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i);
		rgb.shift();
		rgb = rgb.map(function (x) {
			return parseInt(x, 16);
		});
		console.log(rgb);
		var sum = Math.round(
			(parseInt(rgb[0]) * 299 +
				parseInt(rgb[1]) * 587 +
				parseInt(rgb[2]) * 114) /
				1000
		);
		return sum > 128 ? 'black' : 'white';
	}

	function copyToClipboard(text) {
		navigator.clipboard.writeText(text).then(
			() => {
				console.log('Color copied to clipboard!');
			},
			(err) => {
				console.error('Could not copy text: ', err);
			}
		);
	}

	onMount(() => {
		if (selectedGun) {
			colors = colorsData[selectedGun]?.colors || [];
			console.log(colors);
		}
	});

	$: if (selectedGun) {
		colors = colorsData[selectedGun]?.colors || [];
		console.log(colors);
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
						>{color}</span
					>
				</div>
			{/each}
		</div>
		<div class="image-container">
			<img
				id="gun-image"
				src={`${import.meta.env.BASE_URL}/${pixelated ? 'pixelated' : 'skins'}/${colorsData[selectedGun]?.type}/${selectedGun}.png`}
				alt={selectedGun}
				style="pointer-events: auto;"
			/>
		</div>
	</div>
	<div class="dropdown">
		<select id="guns" name="weapon_name" bind:value={selectedGun}>
			<option value="">Select a gun</option>
			<option value="abyssal">Abyssal</option>
			<option value="altitude">Altitude</option>
			<option value="araxys">Araxys</option>
			<option value="aristocrat">Aristocrat</option>
			<option value="avalanche">Avalanche</option>
			<option value="blastx">Blastx</option>
			<option value="black_market">Black Market</option>
			<option value="celestial">Celestial</option>
			<option value="champions_2021" selected>Champions 2021</option>
			<option value="champions_2022">Champions 2022</option>
			<option value="champions_2023">Champions 2023</option>
			<option value="chromedek">Chromedek</option>
			<option value="chronovoid">Chronovoid</option>
			<option value="cryostasis">Cryostasis</option>
			<option value="crimsonbeast">Crimsonbeast</option>
			<option value="daydreams">Daydreams</option>
			<option value="doodle_buds">Doodle Buds</option>
			<option value="ego">Ego</option>
			<option value="elderflame">Elderflame</option>
			<option value="emberclad">Emberclad</option>
			<option value="endeavour">Endeavour</option>
			<option value="fortunes_hand">Fortune's Hand</option>
			<option value="forsaken">Forsaken</option>
			<option value="gaias_vengeance">Gaia's Vengeance</option>
			<option value="galleria">Galleria</option>
			<option value="glitchpop">Glitchpop</option>
			<option value="holomoku">Holomoku</option>
			<option value="horizon">Horizon</option>
			<option value="imperium">Imperium</option>
			<option value="ion">Ion</option>
			<option value="kohaku_matsuba">Kohaku Matsuba</option>
			<option value="kuronami">Kuronami</option>
			<option value="luna">Luna</option>
			<option value="luxe">Luxe</option>
			<option value="magepunk">Magepunk</option>
			<option value="mk_vii_liberty">MK VII Liberty</option>
			<option value="minima">Minima</option>
			<option value="mystbloom">Mystbloom</option>
			<option value="nebula">Nebula</option>
			<option value="neo_frontier">Neo Frontier</option>
			<option value="neptune">Neptune</option>
			<option value="no_limits">No Limits</option>
			<option value="nunca_olvidados">Nunca Olvidados</option>
			<option value="oni">Oni</option>
			<option value="origin">Origin</option>
			<option value="orion">Orion</option>
			<option value="overdrive">Overdrive</option>
			<option value="primordium">Primordium</option>
			<option value="prime">Prime</option>
			<option value="prime_ii">Prime II</option>
			<option value="prism">Prism</option>
			<option value="prism_ii">Prism II</option>
			<option value="protocol_781-a">Protocol 781-A</option>
			<option value="radiant_crisis_001">Radiant Crisis 001</option>
			<option value="radiant_entertainment_system"
				>Radiant Entertainment System</option
			>
			<option value="reaver">Reaver</option>
			<option value="recon">Recon</option>
			<option value="reverie">Reverie</option>
			<option value="rgx_11z_pro">RGX 11Z Pro</option>
			<option value="ruination">Ruination</option>
			<option value="rush">Rush</option>
			<option value="sakura">Sakura</option>
			<option value="sarmad">Sarmad</option>
			<option value="sentinels_of_light">Sentinels of Light</option>
			<option value="sensation">Sensation</option>
			<option value="silvanus">Silvanus</option>
			<option value="singularity">Singularity</option>
			<option value="smite">Smite</option>
			<option value="snowfall">Snowfall</option>
			<option value="sovereign">Sovereign</option>
			<option value="soulstrife">Soulstrife</option>
			<option value="spectrum">Spectrum</option>
			<option value="spline">Spline</option>
			<option value="switchback">Switchback</option>
			<option value="team_ace">Team Ace</option>
			<option value="tethered_realms">Tethered Realms</option>
			<option value="tigris">Tigris</option>
			<option value="titanmail">Titanmail</option>
			<option value="undercity">Undercity</option>
			<option value="valorant_go_vol_1">Valorant Go Vol 1</option>
			<option value="valorant_go_vol_2">Valorant Go Vol 2</option>
			<option value="valiant_hero">Valiant Hero</option>
			<option value="wasteland">Wasteland</option>
			<option value="winterwunderland">Winterwunderland</option>
			<option value="xenohunter">Xenohunter</option>
			<option value="xerofang">Xerofang</option>
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
		pointer-events: none;
	}

	#gun-image {
		pointer-events: auto;
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
		font-family: 'The Future', monospace;
		font-weight: bold;
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
		font-family: 'Valorant';
	}

	.dropdown select:focus {
		outline: none;
		border-color: #4caf50;
	}
</style>
