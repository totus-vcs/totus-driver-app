



const InvisiBox = ({ text }) => {
    return <div class="col">
        <div class="h-100 border-0 shadow-sm p-xxl-3">
        
            <div class="card-body">
                <div class="d-flex align-items-center pb-2 pb-md-3 mb-0">
                    <div class="ps-4">
                        {/* <h3 class="fs-lg fw-normal text-light opacity-70 mb-2"> 2022 </h3> */}
                        <h4 class="h3 text-light lh-1 mb-0">
                            <span data-monthly-price>{text}</span>
                            <span class="fs-sm fw-normal opacity-70"></span>
                        </h4>
                    </div>
                </div>
                {/* <ul class="list-unstyled fs-sm pb-md-3 mb-3">
                    {items}

                </ul> */}
            </div>
   
            </div>
    </div>

}

export default InvisiBox; 