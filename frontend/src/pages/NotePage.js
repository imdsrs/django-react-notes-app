import React, { useState, useEffect } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";
import { ReactComponent as ArrowLeft } from "../assets/arrow-left.svg";

const NotePage = () => {
    const { idValue } = useParams();
    let noteId = idValue;
    let navigate = useNavigate();
    let [note, setNote] = useState(null);

    let getNote = async () => {
        let response = await fetch(`/api/notes/${noteId}`);
        let data = await response.json();
        //console.log(data);
        setNote(data);
    };

    // let updateNote = async () => {
    //     await fetch(`api/notes/${noteId}/update`, {
    //         method: "PUT",
    //         headers: {
    //             "Content-Type": "application/json",
    //         },
    //         body: JSON.stringify(note),
    //     });
    // };

    let updateNote = async () => {
        await fetch(`/api/notes/${noteId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(note),
        });
    };

    let deleteNote = async () => {
        await fetch(`/api/notes/${noteId}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        });
        navigate("/");
    };

    let createNote = async () => {
        await fetch(`/api/notes/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(note),
        });
    };

    let handleSubmit = async () => {
        console.log("Note", note);
        if (noteId !== "new" && !note.body) {
            deleteNote();
            console.log("del");
        } else if (noteId !== "new") {
            updateNote();
            console.log("up");
        } else if (noteId === "new" && note !== null) {
            createNote();
            console.log("cre");
        } else {
            console.log(".....");
        }
        navigate("/");
    };

    useEffect(() => {
        if (noteId !== "new") getNote();
    }, [noteId]);

    return (
        <div className="note">
            <div className="note-header">
                <h3>
                    <ArrowLeft onClick={handleSubmit} />
                </h3>
                {noteId !== "new" ? (
                    <button onClick={deleteNote}>Delete</button>
                ) : (
                    <button onClick={handleSubmit}>Done</button>
                )}
            </div>
            <textarea
                onChange={(e) => {
                    setNote({ ...note, body: e.target.value });
                    console.log(e.target.value);
                }}
                value={note?.body}
            ></textarea>
        </div>
    );
};

export default NotePage;
