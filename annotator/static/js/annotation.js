/**
 * Created by tonnpa on 12/9/16.
 */
function updateAnnotation(annotationID, mark) {
    return $.ajax(prepRequest({
        url: "/annotations/" + annotationID + "/",
        type: "PATCH",
        data: JSON.stringify({
            annotation: mark
        })
    }));
}

function updateAnnotations(annotations) {
    var deferred = [];
    annotations.each(function (idx, entry) {
        deferred.push(updateAnnotation(entry.name, entry.value));
    });
    return deferred;
}