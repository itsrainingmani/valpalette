<script>
  import { quadInOut } from "svelte/easing";
  import { tweened } from "svelte/motion";
  export let color = "#fff";
  export let color_width = 100;
  const progress = tweened(color_width, {
    duration: 500,
    easing: quadInOut,
  });

  $: progress.set(color_width);

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
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
  class="row"
  style={`background: linear-gradient(90deg, ${color} ${$progress * 2}%, #222 0%);`}
  title={color}
  on:click={() => copyToClipboard(color)}
>
  <span class="color-hex" style={`color: ${calcFontColor(color)}; `}
    >{color.toUpperCase()}{" "}<span
      class="copy-msg"
      style={`color: ${calcFontColor(color)}`}>copied to clipboard</span
    ></span
  >
</div>

<style>
  .row {
    position: relative;
    height: 14.2%;
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
    from {
      opacity: 1;
    }
    to {
      opacity: 0;
    }
  }
</style>
