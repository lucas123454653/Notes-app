/**
 * Function to delete a note by its ID.
 * 
 * @param {number} noteId - The ID of the note to be deleted.
 */
function deleteNote(noteId) {
  // Send a POST request to the server to delete the note
  fetch("/delete-note", {
    method: "POST", // Specify the request method as POST
    body: JSON.stringify({ noteId: noteId }), // Send the noteId as JSON
  })
  .then((_res) => {
    // Redirect to the notes page after deletion is complete
    window.location.href = "/notes";
  });
}
