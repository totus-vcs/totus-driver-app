

const TeamMemberIcon = ({ name, role, imageLoc, linkedInUrl }) => {
    return <div class="col-3">
    <div class="card card-hover border-0 bg-transparent">
      <div class="position-relative">
        <img
          src={imageLoc}
          class="rounded-3"
          height={320}
          alt={name}
        />
        <div class="card-img-overlay d-flex flex-column align-items-center justify-content-center rounded-3">
          <span class="position-absolute top-0 start-0 w-100 h-100 bg-dark opacity-25 rounded-3"></span>
          <div class="position-relative d-flex zindex-2">
            {linkedInUrl &&
            <a
              href={linkedInUrl}
              class="btn btn-icon btn-secondary btn-linkedin btn-sm bg-white me-2"
            >
              <i class="bx bxl-linkedin"></i>
            </a>}
          </div>
        </div>
      </div>
      <div class="card-body text-center p-3">
        <h3 class="fs-lg fw-semibold pt-1 mb-2">{name}</h3>
        <p class="fs-sm mb-0">{role}</p>
      </div>
    </div>
    </div>

}

export default TeamMemberIcon; 

