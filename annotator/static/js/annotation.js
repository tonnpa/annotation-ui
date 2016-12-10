/**
 * Created by tonnpa on 12/9/16.
 */

function addAnnotation(drugID, cui, mdr1, mark) {
    console.log(JSON.stringify({
            cui: cui,
            mdr1: mdr1,
            annotation: mark
        }));
    return $.ajax(prepRequest({
        url: "/annotations/",
        type: "POST",
        data: JSON.stringify({
            key: drugID,
            cui: cui,
            mdr1: mdr1,
            annotation: mark
        })
    }));
}

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