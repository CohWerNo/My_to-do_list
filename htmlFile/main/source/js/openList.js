function pageCreate() {
    /**
     * Открывает лист на странице
     * 
     * index: Number -- число листа которое будет открыто
     */
    function openList(index = 0) {
        window.location.href = "/list" + index;
    }

    const windowLists = document.getElementById("windowLists");
    Array.from(windowLists.children).forEach(function(child, index) {
        child.addEventListener("click", function(event) {
            openList(index);
        });
    });
}