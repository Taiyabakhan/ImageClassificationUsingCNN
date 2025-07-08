function startLoading() {
  document.getElementById("spinner").style.display = "block";
  document.getElementById("loadingBar").style.display = "block";
  let progress = document.getElementById("loadingProgress");
  progress.style.width = "0%";
  let i = 0;
  let interval = setInterval(() => {
    if (i >= 100) clearInterval(interval);
    progress.style.width = i + "%";
    i += 10;
  }, 100);
}
