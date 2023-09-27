import { BrowserRouter, HashRouter, Routes, Route } from "react-router-dom";

import Navbar from "./scenes/navbar";

import 'atropos/css'

import ScrollToTop from "./components/ScrollToTop";



function App() {
  return (
    <HashRouter>
      <ScrollToTop/>

    <div className="App">
      <header className="App-header">

        {/* <!-- Page loading spinner --> */}
        <div className="page-loading active">
          <div className="page-loading-inner">
            <div className="page-spinner"></div>
            <span>Loading...</span>
          </div>
        </div>

        {/* <!-- Page wrapper for sticky footer --> */}
        {/* <!-- Wraps everything except footer to push footer to the bottom of the page if there is little content --> */}
        <main className="page-wrapper">

          {/* Components */}
          <Navbar />
          
             
        </main>

      </header>
    </div>
    </HashRouter>

  );
}

export default App;
