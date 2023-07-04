import React from "react";
import { Link } from "react-router-dom";

let getTitle = (note) => {
    const title = note.body.split("\n")[0];
    if (title.length > 45) {
        return title.slice(0, 30) + "...";
    }
    return title;
};

let getDate = (note) => {
    return new Date(note.updated).toLocaleDateString();
};

let getContent = (note) => {
    let title = getTitle(note);
    let content = note.body.replaceAll("\n", " ");
    content = content.replace(title, "");

    if (content.length > 45) {
        return content.slice(0, 45) + "...";
    } else {
        return content;
    }
};

const ListItem = ({ note }) => {
    return (
        <Link to={`/note/${note.id}`}>
            <div className="notes-list-item">
                <h3>hello: {getTitle(note)}</h3>
                <p>
                    <span>{getDate(note)}</span>
                    {getContent(note)}
                </p>
            </div>
        </Link>
    );
};

export default ListItem;
