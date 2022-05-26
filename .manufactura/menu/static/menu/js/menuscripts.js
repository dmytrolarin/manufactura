function linklist(what){
    var selectedopt=what.options[what.selectedIndex]
    if (document.getElementById && selectedopt.getAttribute("target")=="new")
    window.open(selectedopt.value)
    else
    window.location=selectedopt.value
    }