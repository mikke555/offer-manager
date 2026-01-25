const categoryColors = {
  Gaming: "bg-violet-100 text-violet-500",
  Tech: "bg-sky-100 text-sky-500",
  Health: "bg-rose-100 text-rose-500",
  Nutrition: "bg-lime-100 text-lime-600",
  Fashion: "bg-pink-100 text-pink-500",
  Finance: "bg-amber-100 text-amber-600",
};

const CategoryBadge = ({ name }: { name: keyof typeof categoryColors }) => {
  const cn = `${categoryColors[name]} text-sm rounded-full px-3 py-1`;

  return <div className={cn}>{name}</div>;
};

export default CategoryBadge;
