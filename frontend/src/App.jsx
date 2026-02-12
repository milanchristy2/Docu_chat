import Navbar from "./components/Navbar";
import Upload from "./components/Upload";
import Chat from "./components/Chat";

function App() {
  return (
    <div className="min-vh-100 bg-light">

      <Navbar />

      <div className="container-fluid py-4 px-5">
        <Upload />
        <Chat />
      </div>

    </div>
  );
}

export default App;
