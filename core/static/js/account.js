/**
 * Created by musale on 7/10/16.
 */
function toggle(source) {
    checkboxes = document.getElementsByName('selection');
    $("button[type='submit']").attr("disabled", !source.checked);
    for(var i in checkboxes)
        checkboxes[i].checked = source.checked;
}
var all_checkboxes = $("input[type='checkbox']"),
    submitButt = $("button[type='submit']");

all_checkboxes.click(function() {
    submitButt.attr("disabled", !all_checkboxes.is(":checked"));
});