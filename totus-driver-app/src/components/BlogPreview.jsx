import { Link } from "react-router-dom"; 


const BlogPreview = ({ bgImage, pageref, date, title, previewText, authorAvatar}) => {
  return <article className="card border-0 shadow-sm overflow-hidden mb-4">
    <div className="row g-0">
      <div
        className="col-sm-4 position-relative bg-position-center bg-repeat-0 bg-size-cover"
        style={{
          backgroundImage: bgImage,
          minHeight: "15rem",
        }}
      >
        <Link
          to={pageref}
          className="position-absolute top-0 start-0 w-100 h-100"
          aria-label="Read more"
        />

      </div>
      <div className="col-sm-8">
        <div className="card-body">
          <div className="d-flex align-items-center mb-3">
            <span className="fs-sm text-muted">
              {date}
            </span>
          </div>
          <h3 className="h4">

            <Link to={pageref}>
              {title}
            </Link>
          </h3>


          <p>
            {previewText}
          </p>
          <hr className="my-4" />
          {authorAvatar}
        </div>
      </div>
    </div>
  </article>
}

export default BlogPreview