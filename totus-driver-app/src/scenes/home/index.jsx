// {/* <!-- Hero section with layer parallax gfx --> */}


import QuickLinks from "./QuickLinks";
import HomeInfo from "./HomeInfo";
// import AuditTracking from "./AuditTracking";
import Team from "./Team";
import WhatsNew from "./WhatsNew"; 


const Home = () => {
    return <div>
           
        <HomeInfo/>  
        <WhatsNew/>
        <QuickLinks/>
        {/* <AuditTracking/> */}
        <Team/>
        
    </div>
}

export default Home; 