function setupZoomPage(entries) {
    window.addEventListener("load", function() {
        container = document.createElement("div");
        sidebar = document.createElement("div");
        display = document.createElement("div");
        mainSheet = document.createElement("link");
        zoomSheet = document.createElement("link");

        container.classList.add("zoomContainer");
        sidebar.classList.add("sidebar");
        display.classList.add("display");

        mainSheet.rel = "stylesheet";
        mainSheet.type = "text/css";
        mainSheet.href = "/style.css";
        zoomSheet.rel = "stylesheet";
        zoomSheet.type = "text/css";
        zoomSheet.href = "/zoom.css";

        container.appendChild(sidebar);
        container.appendChild(display);
        document.body.appendChild(container);
        document.body.appendChild(mainSheet);
        document.body.appendChild(zoomSheet);

        currentIdx = 0;
        function switchView(idx) {
            sidebar.children[currentIdx].classList.remove("selected");
            sidebar.children[idx].classList.add("selected");
            display.children[currentIdx].hidden = true;
            display.children[idx].hidden = false;
            currentIdx = idx;
        }

        for (let i = 0; i < entries.length; i++) {
            // Hack to prevent i from updating when the loop continues
            callback = () => switchView((() => i)());

            if (entries[i].icon == undefined) {
                iconDiv = document.createElement("div");
                iconSpan = document.createElement("span");

                iconSpan.innerText = entries[i].name;

                iconDiv.addEventListener("click", callback);
                iconDiv.addEventListener("mouseover", callback);

                iconDiv.appendChild(iconSpan);
                sidebar.appendChild(iconDiv);
            } else {
                icon = document.createElement("img");

                icon.classList.add("small");
                icon.src = entries[i].icon;
                icon.title = entries[i].name;

                icon.addEventListener("click", callback);
                icon.addEventListener("mouseover", callback);

                sidebar.appendChild(icon);
            }

            img = document.createElement("img");
            img.src = entries[i].src;
            img.hidden = true;

            display.appendChild(img);
        }

        sidebar.children[0].classList.add("selected");
        display.children[0].hidden = false;
    })
}
