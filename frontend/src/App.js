import "./App.css";
import Header from "./components/Header";
import NotesListPage from "./pages/NotesListPage";
import NotePage from "./pages/NotePage";

import { HashRouter as Router, Routes, Route } from "react-router-dom";

function App() {
    return (
        <Router>
            <div className="container dark">
                <div className="app">
                    <Header />
                    {/* My App */}
                    <Routes>
                        <Route path="/" exact element={<NotesListPage />} />
                        <Route path="/note/:idValue" element={<NotePage />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;
